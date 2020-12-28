#        Servirtium: Service Virtualized HTTP
#
#        Copyright (c) 2019, Paul Hammant and committers
#        All rights reserved.
#
#        Redistribution and use in source and binary forms, with or without
#        modification, are permitted provided that the following conditions are met:
#
#        1. Redistributions of source code must retain the above copyright notice, this
#        list of conditions and the following disclaimer.
#        2. Redistributions in binary form must reproduce the above copyright notice,
#        this list of conditions and the following disclaimer in the documentation
#        and/or other materials provided with the distribution.
#
#        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#        ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#        WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#        DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#        ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#        LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#        ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#        The views and conclusions contained in the software and documentation are those
#        of the authors and should not be interpreted as representing official policies,
#        either expressed or implied, of the Servirtium project.
import itertools
import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from json import JSONDecodeError
from pyexpat import ExpatError
from xml.dom import minidom

import requests
from servirtium.interaction_recording import InteractionRecording
from servirtium.interactions import Interaction


def _prune_headers(headers, removables):
    def _to_be_removed(item):
        (key, value) = item
        line = f'{key}: {value}'
        any([line.startswith(removable) for removable in removables])

    return dict(itertools.filterfalse(_to_be_removed, headers.items()))


class Interception:
    def __init__(self,
                 host: str = "default_host",
                 request_header_overrides: dict = None,
                 response_headers_to_remove: list = None) -> None:
        self.host = host
        self.request_header_overrides = request_header_overrides or {}
        self.response_headers_to_remove = response_headers_to_remove or []
        self.current_recording = InteractionRecording()

    def modified_request_headers(self, new_req_headers):
        modified = new_req_headers.copy()
        modified.update(self.request_header_overrides)
        return modified

    def modified_response_headers(self, response):
        return _prune_headers(response.headers, self.response_headers_to_remove)

    def real_service_host(self):
        return self.host.replace('http://', '').replace('https://', '')


# noinspection PyPep8Naming
class RecorderHttpHandler(BaseHTTPRequestHandler):
    interception = Interception()
    markdown_filename = 'default_method'
    mocks_dir = os.getcwd()
    pretty = False

    @staticmethod
    def pretty_print_json_or_xml():
        RecorderHttpHandler.pretty = True

    @staticmethod
    def set_mocks_dir(mocks_dir):
        RecorderHttpHandler.mocks_dir = mocks_dir

    @staticmethod
    def set_markdown_filename(markdown_filename):
        RecorderHttpHandler.markdown_filename = markdown_filename
        RecorderHttpHandler.current_recording = InteractionRecording()
        md_path = RecorderHttpHandler.mocks_dir + os.sep + RecorderHttpHandler.markdown_filename + ".md"
        if os.path.exists(md_path):
            os.remove(md_path)

    # TODO - should override handle() of http.server
    #        instead of do_GET() of BaseHTTPRequestHandler

    def do_GET(self):
        self.process_request("\n")

    def do_DELETE(self):
        self.process_request("\n")

    def do_OPTIONS(self):
        self.process_request("\n")

    def do_POST(self):
        self.process_request_with_body()

    def do_PATCH(self):
        self.process_request_with_body()

    def process_request_with_body(self):
        l = int(self.headers['Content-Length'])
        r = self.rfile.read(l)
        print("r typ " + str(type(r)))
        self.process_request(r.decode("utf-8"))

    def do_PUT(self):
        self.process_request_with_body()


    def prettifyXML(self, xml_string):
        return minidom.parseString(xml_string).toprettyxml(indent="  ")

    def process_request(self, request_body):
        if RecorderHttpHandler.pretty and len(request_body) > 1:
            print("request_body>" + request_body + "<")
            try:
                request_body = json.dumps(json.loads(request_body), indent=2)
            except JSONDecodeError:
                pass

            try:
                request_body = self.prettifyXML(request_body)
            except ExpatError:
                pass

        new_req_headers = dict(self.headers.items())
        new_req_headers.update({'Host': self.interception.real_service_host()})

        response = self.perform_request_on_real_service(new_req_headers, request_body)
        self.send_response(response.status_code)
        ctt = str(response.content, 'utf-8').replace("https://todo-backend-sinatra.herokuapp.com", "http://localhost:61417") \
            .replace("todo-backend-sinatra.herokuapp.com", "localhost:61417").encode("utf-8")

        # Always send Content-Length header and skip Transfer-Encoding header as the response is not chunked
        self.send_header("Content-Length", str(len(ctt)))
        for name, value in sorted(response.headers.items()):
            value = value.replace("https://todo-backend-sinatra.herokuapp.com", "http://localhost:61417")\
                .replace("todo-backend-sinatra.herokuapp.com", "localhost:61417")

            if name != 'Transfer-Encoding':  # skip Transfer-Encoding as we are setting Content-Length
                # TODO: add support for Transfer-Encoding = chunked
                self.send_header(name, value)

        self.end_headers()
        self.wfile.write(response.content)
        rsp_body = str(response.content, encoding='utf-8')
        if RecorderHttpHandler.pretty and len(rsp_body) > 1:
            try:
                rsp_body = json.dumps(json.loads(rsp_body), indent=2)
            except JSONDecodeError:
                pass
        RecorderHttpHandler.interception.current_recording.add_interaction(
            Interaction(http_verb=self.command,
                        request_headers=self.interception.modified_request_headers(new_req_headers),
                        request_body=request_body,
                        request_path=self.path,
                        response_headers=self.interception.modified_response_headers(response),
                        response_body= rsp_body,
                        response_code=response.status_code))
        try:
            os.mkdir(RecorderHttpHandler.mocks_dir)
        except FileExistsError:
            pass

        md_path = RecorderHttpHandler.mocks_dir + os.sep + RecorderHttpHandler.markdown_filename + ".md"
        f = open(md_path, "a")
        f.write(RecorderHttpHandler.interception.current_recording.last_interaction_to_markdown_string())
        f.close()

    def perform_request_on_real_service(self, new_req_headers, request_body):
        if self.command == "GET":
            response = requests.request(self.command, RecorderHttpHandler.interception.host + self.path,
                                        headers=new_req_headers)
        else:
            response = requests.request(self.command, RecorderHttpHandler.interception.host + self.path,
                                        headers=new_req_headers, data=request_body)
        return response


def set_mocks_dir(mocks_dir):
    RecorderHttpHandler.set_mocks_dir(mocks_dir)

def set_markdown_filename(filename):
    RecorderHttpHandler.set_markdown_filename(filename)

def set_real_service(host):
    RecorderHttpHandler.interception.host = host

def pretty_print_json_or_xml():
    RecorderHttpHandler.pretty_print_json_or_xml()

def set_request_header_replacements(replacements):
    RecorderHttpHandler.interception.request_header_overrides = replacements


def set_response_header_removals(removals):
    RecorderHttpHandler.interception.response_headers_to_remove = removals


def start():
    server_address = ('localhost', 61417)
    try:
        httpd = HTTPServer(server_address, RecorderHttpHandler)
    except OSError  as e:
        if "Address already in use" in str(sys.exc_info()[1]):
            assert False, "Address 'localhost:61417' is in use already - can't start recorder"
        raise e
    httpd.serve_forever()


if __name__ == "__main__":
    start()
