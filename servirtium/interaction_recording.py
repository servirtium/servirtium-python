from interactions import Interaction
from markup import Markup

REQ_HEADER_TITLE = 'Request headers recorded for playback:'
REQ_BODY_TITLE = 'Request body recorded for playback ():'
RESPONSE_HEADER_TITLE = 'Response headers recorded for playback:'


class InteractionRecording:
    def __init__(self):
        self.interactions = []

    def add_interaction(self, interaction: Interaction):
        self.interactions.append(interaction)

    def to_markdown_string(self) -> str:
        return '\n'.join(
            [_as_markup(ix, interaction).as_markdown() for ix, interaction in enumerate(self.interactions)])


def _as_markup(index, interaction) -> Markup:
    return Markup().header(2, _interaction_header(index, interaction)) \
        .section(3, REQ_HEADER_TITLE, _headers_to_string(interaction.request_headers)) \
        .section(3, REQ_BODY_TITLE, interaction.request_body if not '' else '\n') \
        .section(3, RESPONSE_HEADER_TITLE, _headers_to_string(interaction.response_headers)) \
        .section(3, _response_body_title(interaction), interaction.response_body)


def _response_body_title(interaction: Interaction):
    return f"Response body recorded for playback ({interaction.response_code}: {interaction.response_type}):"


def _headers_to_string(headers: {}):
    return '\n'.join([f'{k}: {v}' for (k, v) in headers.items()])


def _interaction_header(index, interaction):
    return f'Interaction {index}: {interaction.http_verb} {interaction.path}'
