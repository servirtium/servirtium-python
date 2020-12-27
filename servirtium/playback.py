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

from servirtium.markdown_parser import SimpleMarkdownParser, headers_from


class MockServiceHttpHandler(BaseHTTPRequestHandler):
    markdown_filename = "default_value"

    @staticmethod
    def set_markdown_filename(markdown_filename):
        MockServiceHttpHandler.markdown_filename = markdown_filename

    # TODO - should override handle() of http.server
    #        instead of do_GET() of BaseHTTPRequestHandler

    def do_GET(self):
        recording = parser.get_recording_from_method_name(MockServiceHttpHandler.markdown_filename)

        if parser.is_valid_path(self.path) and recording:
            interaction = next(iter([i for i in recording.interactions if i.path == self.path]))
            if not interaction:
                self.send_error(HTTPStatus.NOT_FOUND, f"Unknown {self.path} path")
                return

            request_headers = headers_from(str(self.headers).strip())

            if interaction.request_headers == request_headers or True:  # Headers currently don't match
                self.send_response(200)
                self.send_header("Content-type", "text/html")

                # if False:  # To fix, currently won't send with headers from .md file
                #     for key, value in interaction.response_headers.items():
                #         self.send_header(key.strip(), value)

                self.end_headers()
                self.wfile.write(bytes(interaction.response_body, "utf-8"))
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Unknown file path")


parser = SimpleMarkdownParser()


def start():
    server_address = ('localhost', 61417)
    httpd = HTTPServer(server_address, MockServiceHttpHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()
