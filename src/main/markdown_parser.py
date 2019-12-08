import os

from src.main.servirtium_recording import MockRecording, Interaction


class SimpleMarkdownParser:

    @staticmethod
    def get_recording_from_name(method_name: str, mock_recordings: [MockRecording]) -> MockRecording:
        recordings = list(filter(lambda mock: mock.file_name.replace('.md', '') in method_name, mock_recordings))
        return recordings[0] if len(recordings) > 0 else None

    @staticmethod
    def is_valid_path(path, mock_recordings: [MockRecording]) -> bool:
        return bool(filter(lambda x: x.path == path, [i.interactions for i in [m for m in mock_recordings]]))

    @staticmethod
    def get_dict_from_headers_string(headers_string) -> {}:
        out = {}
        lines = headers_string.split('\n')

        for line in lines:
            line_split = [l.strip().replace('\n', '') for l in line.split(':')]
            out[line_split[0]] = line_split[1]
        return out

    @staticmethod
    def __get_markdown_file_strings(mocks_path) -> [(str, str)]:
        file_strings = []

        for filename in os.listdir(mocks_path):
            file_path = os.path.join(mocks_path, filename)
            file = open(file_path, "r")
            file_strings.append((file.read(), filename))

        return file_strings

    @staticmethod
    def get_headers_dict(header_string) -> dict:
        out = {}
        header_lines = header_string.split('\n')

        for line in header_lines:
            line_split = [l.strip() for l in line.split(':')]
            out[line_split[0]] = line_split[1]
        return out

    def get_recordings(self, mocks_path) -> [MockRecording]:
        markdown_raw_strings = self.__get_markdown_file_strings(mocks_path)
        return [self.__parse_markdown_string(s1, s2) for (s1, s2) in markdown_raw_strings]

    def __parse_markdown_string(self, markdown_string, file_name) -> MockRecording:

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
            request_headers = self.get_headers_dict(request_headers_string)
            request_body = clean_strings[2].split('```')[1].strip()

            response_headers_string = clean_strings[3].split('```')[1].strip()
            response_headers = self.get_headers_dict(response_headers_string)
            response_body = clean_strings[4].split('```')[1].strip()

            recording_interactions.append(Interaction(request_path=request_path, request_headers=request_headers, request_body=request_body,
                             response_headers=response_headers, response_body=response_body))

        return MockRecording(file_name=file_name, interactions=recording_interactions)
