import os

from servirtium.servirtium_recording import MockRecording, Interaction


class SimpleMarkdownParser:

    markdown_files = []
    recordings = []

    def get_recording_from_method_name(self, method_name: str) -> MockRecording:
        recordings = list(filter(lambda mock: mock.file_name.replace('.md', '') in method_name, self.recordings))
        return recordings[0] if len(recordings) > 0 else None

    def is_valid_path(self, path: [MockRecording]) -> bool:
        return bool(filter(lambda x: x.path == path, [i.interactions for i in [m for m in self.recordings]]))

    @staticmethod
    def get_dict_from_headers_string(headers_string) -> {}:
        out = {}
        lines = headers_string.split('\n')

        for line in lines:
            line_split = [l.strip().replace('\n', '') for l in line.split(':')]
            out[line_split[0]] = line_split[1]
        return out

    @staticmethod
    def get_markdown_file_strings(mocks_path) -> [(str, str)]:
        file_strings = []

        for filename in os.listdir(mocks_path):
            file_path = os.path.join(mocks_path, filename)
            file = open(file_path, "r")
            file_strings.append((file.read(), filename))

        return file_strings

    def _set_mock_files(self, mock_files: [(str, str)]):
        for (name, content) in mock_files:
            SimpleMarkdownParser.markdown_files.append((name, content))
        self.recordings = [SimpleMarkdownParser.parse_markdown_string(s1, s2) for (s1, s2) in self.markdown_files]

    @staticmethod
    def parse_markdown_string(markdown_string, file_name) -> MockRecording:

        interaction_strings = ["## Interaction"+x for x in markdown_string.split("## Interaction") if len(x)]
        recording_interactions = list()

        for interaction in interaction_strings:
            raw_strings = interaction.split("##")
            clean_strings = []

            for string in raw_strings:
                if len(string):
                    clean_strings.append(string.strip().replace('#', ''))

            interaction_description = clean_strings[0]
            interaction_split = interaction_description.split(' ')
            request_path = interaction_split[len(interaction_split) - 1]

            request_headers_string = clean_strings[1].split('```')[1].strip()
            request_headers = SimpleMarkdownParser.get_dict_from_headers_string(request_headers_string)
            request_body = clean_strings[2].split('```')[1].strip()

            response_headers_string = clean_strings[3].split('```')[1].strip()
            response_headers = SimpleMarkdownParser.get_dict_from_headers_string(response_headers_string)
            response_body = clean_strings[4].split('```')[1].strip()

            recording_interactions.append(Interaction(request_path=request_path, request_headers=request_headers, request_body=request_body,
                             response_headers=response_headers, response_body=response_body))

        return MockRecording(file_name=file_name, interactions=recording_interactions)
