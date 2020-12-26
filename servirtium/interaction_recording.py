from servirtium.interactions import Interaction
from servirtium.markup import Markup

REQ_HEADER_TITLE = 'Request headers recorded for playback:'
REQ_BODY_TITLE = 'Request body recorded for playback ():'
RESPONSE_HEADER_TITLE = 'Response headers recorded for playback:'


class InteractionRecording:
    def __init__(self):
        self.interaction_num = -1
        self.last_interaction = {}

    def add_interaction(self, interaction: Interaction):
        self.interaction_num = self.interaction_num + 1
        self.last_interaction = interaction

    def last_interaction_to_markdown_string(self) -> str:
        return _as_markup(self.interaction_num, self.last_interaction).as_markdown()


def _as_markup(index, interaction) -> Markup:
    return Markup().header(2, _interaction_header(index, interaction)) \
        .section(3, REQ_HEADER_TITLE, _headers_to_string(interaction.request_headers)) \
        .section(3, REQ_BODY_TITLE, interaction.request_body if not '' else '\n') \
        .section(3, RESPONSE_HEADER_TITLE, _headers_to_string(interaction.response_headers)) \
        .section(3, _response_body_title(interaction), interaction.response_body)


def _response_body_title(interaction: Interaction):

    attr = ""
    if hasattr(interaction, 'response_type'):
        attr = interaction.response_type

    return f"Response body recorded for playback ({interaction.response_code}: {attr}):"


def _headers_to_string(headers: {}):
    return '\n'.join([f'{k}: {v}' for (k, v) in headers.items()])


def _interaction_header(index, interaction):
    return f'Interaction {index}: {interaction.http_verb} {interaction.path}'
