import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests
from definitions import MOCKS_DIR
from servirtium.interactions import Interaction
from servirtium.playback import SimpleMarkdownParser


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


def hdr_replacements(headers, replacements):
    new_headers = {}
    for k, v in headers.items():
        if k in replacements.keys():
            new_headers[k] = replacements[k]
        else:
            new_headers[k] = v

    return new_headers


class RecorderHttpHandler(BaseHTTPRequestHandler):
    host = "default_host"
    replace_request_headers_in_recording = {}
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

        test_file = parser.get_recording_from_method_name(RecorderHttpHandler.invoking_method)
        response = requests.get(RecorderHttpHandler.host + self.path, headers=new_req_headers)

        self.send_response(response.status_code)
        self.end_headers()
        self.wfile.write(response.content)

        RecorderHttpHandler.current_recording.add_interaction(
            Interaction(request_headers=hdr_replacements(new_req_headers, RecorderHttpHandler.replace_request_headers_in_recording),
                        request_body=request_body, request_path=self.path, response_headers=response.headers,
                        response_body=(str(response.content, encoding='utf-8')), response_code=response.status_code))

        if len(RecorderHttpHandler.current_recording.interactions) == len(test_file.interactions):  # Last interaction
            f = open(MOCKS_DIR + RecorderHttpHandler.invoking_method.replace("test_", '') + ".md", "w+")
            f.write(RecorderHttpHandler.current_recording.to_markdown_string())
            f.close()


parser = SimpleMarkdownParser()


def set_markdown_files(markdown_path):
    files = parser.get_markdown_file_strings(markdown_path)
    parser._set_mock_files(files)


def set_real_host(host):
    RecorderHttpHandler.host = host


def set_request_header_replacements(replacements):
    RecorderHttpHandler.replace_request_headers_in_recording = replacements


def start():
    server_address = ('localhost', 8099)
    httpd = HTTPServer(server_address, RecorderHttpHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    start()


