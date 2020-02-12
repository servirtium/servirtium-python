class Header:
    def __init__(self, level: int, text: str):
        self.level = level
        self.text = text

    def as_markdown(self):
        return f'{"#" * self.level} {self.text}'


class CodeBlock:
    def __init__(self, code: str):
        self.code = code.strip()

    def as_markdown(self):
        return f'```\n{self.code}\n```'


class Markup:
    def __init__(self):
        self.elements = []

    def header(self, level: int, text: str):
        self.elements.append(Header(level, text))
        return self

    def code_block(self, text: str):
        self.elements.append(CodeBlock(text))
        return self

    def as_markdown(self):
        return '\n'.join([e.as_markdown() for e in self.elements]) + '\n'
