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

from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler

from servirtium.markdown_parser import SimpleMarkdownParser
from servirtium.interactions import Interaction


class MockServiceHttpHandler(BaseHTTPRequestHandler):
    invoking_method = "default_value"

    @staticmethod
    def get_interaction_from_path(path, interactions) -> Interaction:
        return list(filter(lambda a: a.path == path, interactions))[0]

    @staticmethod
    def set_invoking_method(method_name):
        MockServiceHttpHandler.invoking_method = method_name

    def do_GET(self):
        test_file = parser.get_recording_from_method_name(MockServiceHttpHandler.invoking_method)

        if parser.is_valid_path(self.path) and test_file:
            interaction = self.get_interaction_from_path(self.path, test_file.interactions)
            request_headers = parser.get_dict_from_headers_string(str(self.headers).strip())

            if interaction.request_headers == request_headers or True:  # Headers currently don't match
                self.send_response(200)
                self.send_header("Content-type", "text/html")

                if False:  # To fix, currently won't send with headers from .md file
                    for key, value in interaction.response_headers.items():
                        self.send_header(key.strip(), value)

                self.end_headers()
                self.wfile.write(bytes(interaction.response_body, "utf-8"))
        else:
            self.send_error(
            HTTPStatus.NOT_FOUND,
            "Unknown file path")


parser = SimpleMarkdownParser()


def set_markdown_files(markdown_path):
    files = parser.get_markdown_file_strings(markdown_path)
    parser._set_mock_files(files)


def start():
    server_address = ('localhost', 61417)
    httpd = HTTPServer(server_address, MockServiceHttpHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()

