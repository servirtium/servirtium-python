import os
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

from definitions import MOCKS_DIR
from src.main.mock_recording import Interaction
from src.main.mock_service import SimpleMarkdownParser


class InteractionRecording:

    req_header_title = '### Request headers recorded for playback:'
    req_body_title = '### Request body recorded for playback ():'

    res_header_title = '### Response headers recorded for playback:'

    @staticmethod
    def get_response_body_title(interaction: Interaction):
        return f"### Response body recorded for playback ({interaction.response_code}: {interaction.response_type}):"

    @staticmethod
    def get_interaction_string_title(interaction: Interaction, interactions: [Interaction]) -> str:
        return f'## Interaction {interactions.index(interaction)}: GET {interaction.path}'

    @staticmethod
    def wrap_string(i_string: str):
        return '```\n' + i_string + '\n```'

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

        return '\n\n'.join(lines)


class RecorderHttpHandler(BaseHTTPRequestHandler):
    host = "default_host"
    invoking_method = 'default_method'
    current_recording = InteractionRecording()

    @staticmethod
    def set_invoking_method(method_name):
        RecorderHttpHandler.invoking_method = method_name
        RecorderHttpHandler.current_recording = InteractionRecording()

    def do_GET(self):
        req_headers = self.headers
        replace_values = {'User-Agent': 'Servirtium-Testing', 'Host': self.host.replace('http://', '')}

        for k, v in req_headers.items():
            if k in replace_values.keys():
                del(req_headers[k])
                req_headers[k] = replace_values[k]

        request_body = "\n"

       # if 'content-length' in [x.lower() for x in self.headers.keys()]:
       #     request_body = str(self.rfile.read(self.headers['content-length']), encoding='utf-8')

        test_file = SimpleMarkdownParser.get_recording_from_name(RecorderHttpHandler.invoking_method, mock_recordings)

        response = requests.get(RecorderHttpHandler.host + self.path, headers=req_headers)

        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

        RecorderHttpHandler.current_recording.add_interaction(Interaction(request_headers=req_headers, request_body=request_body, request_path=self.path,
                                                                          response_headers=response.headers, response_body=(str(response.content, encoding='utf-8')),
                                                                          response_code=response.status_code))

        if len(RecorderHttpHandler.current_recording.interactions) == len(test_file.interactions):  # Last interaction
            f = open(MOCKS_DIR + RecorderHttpHandler.invoking_method.replace("test_", '') + ".md", "w+")
            f.write(RecorderHttpHandler.current_recording.to_markdown_string())
            f.close()


parser = SimpleMarkdownParser()
mock_recordings = parser.get_recordings(os.path.dirname(os.path.realpath(__file__)).replace('main', 'mocks'))


def set_real_host(host):
    RecorderHttpHandler.host = host


def start():
    server_address = ('localhost', 8099)
    httpd = HTTPServer(server_address, RecorderHttpHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()


