import os
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler

from src.main.markdown_parser import SimpleMarkdownParser
from src.main.servirtium_recording import Interaction


class MockServiceHttpHandler(BaseHTTPRequestHandler):
    invoking_method = "default_value"

    @staticmethod
    def get_interaction_from_path(path, interactions) -> Interaction:
        return list(filter(lambda a: a.path == path, interactions))[0]

    @staticmethod
    def set_invoking_method(method_name):
        MockServiceHttpHandler.invoking_method = method_name

    def do_GET(self):
        test_file = SimpleMarkdownParser.get_recording_from_name(MockServiceHttpHandler.invoking_method, mock_recordings)

        if SimpleMarkdownParser.is_valid_path(self.path, mock_recordings) and test_file:
            interaction = self.get_interaction_from_path(self.path, test_file.interactions)
            request_headers = SimpleMarkdownParser.get_dict_from_headers_string(str(self.headers).strip())

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
mock_recordings = parser.get_recordings(os.path.dirname(os.path.realpath(__file__)).replace('main', 'mocks'))


def start():
    server_address = ('localhost', 8099)
    httpd = HTTPServer(server_address, MockServiceHttpHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()

