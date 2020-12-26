from servirtium.markup import Markup


def test_renders_code_block():
    code = '''first line
second line
'''
    assert Markup().code_block(code).as_markdown() == '''```
first line
second line

```
'''


def test_renders_headers():
    assert Markup().header(1, "header 1").as_markdown() == '# header 1\n'
    assert Markup().header(2, "header 2").as_markdown() == '## header 2\n'
    assert Markup().header(3, "header 3").as_markdown() == '### header 3\n'


def test_renders_header_and_code_block():
    assert Markup().header(2, "header 2").code_block('''line 1
line 2''').as_markdown() == '''## header 2

```
line 1
line 2
```
'''


def test_renders_titled_section():
    assert Markup().section(3, 'title', '''body 1
body 2''').as_markdown() == '''### title

```
body 1
body 2
```
'''
