import itertools

from interactions import Interaction

REQ_HEADER_TITLE = '### Request headers recorded for playback:'
REQ_BODY_TITLE = '### Request body recorded for playback ():'
RESPONSE_HEADER_TITLE = '### Response headers recorded for playback:'


class InteractionRecording:
    def __init__(self):
        self.interactions = []

    def add_interaction(self, interaction: Interaction):
        self.interactions.append(interaction)

    def to_markdown_string(self) -> str:
        lines = itertools.chain([self.as_markdown(interaction) for interaction in self.interactions])

        return '\n'.join(*lines)

    def as_markdown(self, interaction):
        return [_interaction_string_title(interaction, self.interactions),
                _section(REQ_HEADER_TITLE, _headers_to_string(interaction.request_headers)),
                _section(REQ_BODY_TITLE, interaction.request_body if not '' else '\n'),
                _section(RESPONSE_HEADER_TITLE, _headers_to_string(interaction.response_headers)),
                _section(get_response_body_title(interaction), interaction.response_body)]


def get_response_body_title(interaction: Interaction):
    return f"### Response body recorded for playback ({interaction.response_code}: {interaction.response_type}):"


def _headers_to_string(headers: {}):
    return '\n'.join([f'{k}: {v}' for (k, v) in headers.items()])


def _interaction_string_title(interaction: Interaction, interactions: [Interaction]) -> str:
    return f'## Interaction {interactions.index(interaction)}: {interaction.http_verb} {interaction.path}\n'


def _section(title: str, contents: str):
    return f'{title}\n{_fixed_text_block(contents)}'


def _fixed_text_block(i_string: str):
    return '\n```\n' + i_string + '\n```\n'

