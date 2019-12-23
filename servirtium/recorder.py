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
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests
from definitions import MOCKS_DIR
from servirtium.interactions import Interaction


class InteractionRecording:

    req_header_title = '### Request headers recorded for playback:'
    req_body_title = '### Request body recorded for playback ():'

    res_header_title = '### Response headers recorded for playback:'

    @staticmethod
    def get_response_body_title(interaction: Interaction):
        return f"### Response body recorded for playback ({interaction.response_code}: {interaction.response_type}):"

    @staticmethod
    def get_interaction_string_title(interaction: Interaction, interactions: [Interaction]) -> str:
        return f'## Interaction {interactions.index(interaction)}: {interaction.http_verb} {interaction.path}\n'

    @staticmethod
    def wrap_string(i_string: str):
        return '\n```\n' + i_string + '\n```\n'

    @staticmethod
    def headers_to_string(headers: {}):
        return '\n'.join([f'{k}: {v}' for (k, v) in headers.items()])

    def __init__(self):
        self.interactions = []

    def add_interaction(self, interaction: Interaction):
        self.interactions.append(interaction)

    def to_markdown_string(self) -> str:
        lines = []

        for interaction in self.interactions:
            lines.append(self.get_interaction_string_title(interaction, self.interactions))

            lines.append(self.req_header_title)
            lines.append(self.wrap_string(self.headers_to_string(interaction.request_headers)))
            lines.append(self.req_body_title)
            lines.append(self.wrap_string(interaction.request_body if not '' else '\n'))  # if empty \n else

            lines.append(self.res_header_title)
            lines.append(self.wrap_string(self.headers_to_string(interaction.response_headers)))

            lines.append(self.get_response_body_title(interaction))
            lines.append(self.wrap_string(interaction.response_body))

        return '\n'.join(lines)


def hdr_replacements(headers, replacements):
    new_headers = {}
    for k, v in headers.items():
        if k in replacements.keys():
            new_headers[k] = replacements[k]
        else:
            new_headers[k] = v

    return new_headers


def hdr_removals(headers, removals):
    new_headers = {}
    for k, v in headers.items():
        should_remove = False
        one_line = k + ": " + v
        for rmv in removals:
            if one_line.startswith(rmv):
                should_remove = True
        if not should_remove:
            new_headers[k] = v
    return new_headers


class RecorderHttpHandler(BaseHTTPRequestHandler):
    host = "default_host"
    replace_request_headers_in_recording = {}
    remove_response_headers_in_recording = []
    invoking_method = 'default_method'
    current_recording = InteractionRecording()

    @staticmethod
    def set_invoking_method(method_name):
        RecorderHttpHandler.invoking_method = method_name
        RecorderHttpHandler.current_recording = InteractionRecording()

    def do_GET(self):
        req_headers = self.headers
        new_req_headers = {}

        replace_values = {'Host': self.host.replace('http://', '')}
        for k, v in req_headers.items():
            if k in replace_values.keys():
                new_req_headers[k] = replace_values[k]
            else:
                new_req_headers[k] = v

        request_body = "\n"

        response = requests.get(RecorderHttpHandler.host + self.path, headers=new_req_headers)

        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

        RecorderHttpHandler.current_recording.add_interaction(
            Interaction(request_headers=hdr_replacements(new_req_headers, RecorderHttpHandler.replace_request_headers_in_recording),
                        request_body=request_body, request_path=self.path,
                        response_headers=hdr_removals(response.headers, RecorderHttpHandler.remove_response_headers_in_recording),
                        response_body=(str(response.content, encoding='utf-8')), response_code=response.status_code))

        f = open(MOCKS_DIR + RecorderHttpHandler.invoking_method.replace("test_", '') + ".md", "w+")
        f.write(RecorderHttpHandler.current_recording.to_markdown_string())
        f.close()


def set_markdown_files(markdown_path):
    pass


def set_real_host(host):
    RecorderHttpHandler.host = host


def set_request_header_replacements(replacements):
    RecorderHttpHandler.replace_request_headers_in_recording = replacements


def set_response_header_removals(removals):
    RecorderHttpHandler.remove_response_headers_in_recording = removals


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


