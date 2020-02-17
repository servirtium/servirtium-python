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

from pathlib import Path

from servirtium.interactions import MockRecording, Interaction


class SimpleMarkdownParser:

    def __init__(self):
        self.markdown_files = []
        self.recordings = []

    def get_recording_from_method_name(self, method_name: str) -> MockRecording:
        recordings = [recording for recording in self.recordings if recording.name() in method_name]
        return recordings[0] if recordings else None

    def is_valid_path(self, path: [MockRecording]) -> bool:
        return bool(filter(lambda x: x.path == path, [i.interactions for i in [m for m in self.recordings]]))

    def _set_mock_files(self, mock_files: [(str, str)]):
        for (name, content) in mock_files:
            self.markdown_files.append((name, content))
        self.recordings = [parse_markdown_string(n, c) for (n, c) in self.markdown_files]


def get_markdown_file_strings(mocks_path) -> [(str, str)]:
    return [(f.name, f.read_text()) for f in Path(mocks_path).iterdir() if f.is_file()]


def parse_markdown_string(file_name, markdown_string) -> MockRecording:
    interaction_strings = ["## Interaction" + x for x in markdown_string.split("## Interaction") if len(x)]

    return MockRecording(file_name=file_name,
                         interactions=[_parse_interaction(interaction) for interaction in interaction_strings])


def _parse_interaction(interaction):
    http_verb = interaction.split("\n")[0].split(" ")[3]
    clean_strings = [s for s in interaction.split("##") if len(s)]

    _checking(clean_strings, 1, '# Request headers recorded for playback:', 'request headers')
    _checking(clean_strings, 2, '# Request body recorded for playback (', "request body")
    _checking(clean_strings, 3, '# Response headers recorded for playback:', 'response headers')
    _checking(clean_strings, 4, '# Response body recorded for playback (', 'response body')

    response_body, response_code = _response(clean_strings)

    return Interaction(request_path=(_request_path(clean_strings)),
                       request_headers=(_request_headers(clean_strings)),
                       request_body=(_code_block_body(clean_strings, 2)),
                       response_headers=(headers_from(_code_block_body(clean_strings, 3))),
                       response_body=response_body,
                       response_code=response_code,
                       http_verb=http_verb)


def _request_path(clean_strings):
    interaction_description = clean_strings[0]
    interaction_split = interaction_description.split(' ')
    return interaction_split[-1].strip()


def _request_headers(clean_strings):
    split = clean_strings[1].split('\n```\n')
    request_headers_string = split[1].strip()
    return headers_from(request_headers_string)


def _response(clean_strings):
    resp_body_chunk = clean_strings[4]
    response_code = resp_body_chunk.split('\n```\n')[0].split("(")[1].split(":")[0]
    response_body = resp_body_chunk.split('\n```\n')[1].strip()
    return response_body, response_code


def _code_block_body(clean_strings, index):
    return clean_strings[index].split('\n```\n')[1].strip()


def _checking(clean_strings, index, expected_prefix, description):
    assert clean_strings[index].startswith(expected_prefix), f"Servirtium {description} line missing from markdown"


def headers_from(headers_string) -> {}:
    out = {}
    lines = headers_string.split('\n')

    for line in lines:
        line_split = [token.strip().replace('\n', '') for token in line.split(':')]
        out[line_split[0]] = line_split[1]
    return out
