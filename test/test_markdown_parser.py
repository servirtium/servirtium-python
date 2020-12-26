import sys
from unittest.mock import patch

import pytest

from definitions import ROOT_DIR
from servirtium.markdown_parser import SimpleMarkdownParser, parse_markdown_string, get_markdown_file_strings


@patch('markdown_parser.SimpleMarkdownParser.get_file_content')
def qqtest_bad_markdown_means_no_recordings(mock_get_file_content):
    mock_get_file_content.return_value = 'abc 123'
    recording = SimpleMarkdownParser().get_recording_from_method_name("foo")
    assert recording is None


def test_corrupt_request_headers_in_markdown_yields_error():
    try:
        parse_markdown_string("", """## Interaction 0: GET /path/to/resource

### XXXXXXXX recorded for playback:

nothing else important to test

""")
        pytest.fail()
    except AssertionError:
        assert "Servirtium request headers line missing from markdown" in str(sys.exc_info()[1])


def test_corrupt_request_body_in_markdown_yields_error():
    try:
        parse_markdown_string("", """## Interaction 0: GET /path/to/resource

### Request headers recorded for playback:

```
a: b
```

### xxxxxxxx recorded for playback (application/xml):

nothing else important to test

""")
        pytest.fail()
    except AssertionError:
        assert "Servirtium request body line missing from markdown" in str(sys.exc_info()[1])


def test_corrupt_response_body_in_markdown_yields_error():
    parser = SimpleMarkdownParser()
    try:
        parse_markdown_string("", """## Interaction 0: GET /path/to/resource

### Request headers recorded for playback:

```
a: b
```

### Request body recorded for playback (application/xml):

```
x
```

### xxxxxx recorded for playback:

nothing else important to test

""")
        pytest.fail()
    except AssertionError:
        assert "Servirtium response headers line missing from markdown" in str(sys.exc_info()[1])


def test_corrupt_response_body_in_markdown_yields_error1():
    parser = SimpleMarkdownParser()
    try:
        parse_markdown_string("", """## Interaction 0: GET /path/to/resource

### Request headers recorded for playback:

```
a: b
```

### Request body recorded for playback (application/xml):

```
x
```

### Response headers recorded for playback:

```
a: b
```

### Xxxxxx recorded for playback (application/xml):

nothing else important to test

""")
        pytest.fail()
    except AssertionError:
        assert "Servirtium response body line missing from markdown" in str(sys.exc_info()[1])


def test_good_markdown_results_in_recording_object():
    parser = SimpleMarkdownParser()
    files = get_markdown_file_strings(ROOT_DIR + "/test/mocks1")
    parser._set_mock_files(files)
    recording = parser.get_recording_from_method_name("foo")

    assert recording is not None
    assert len(recording.interactions) is 2

    i = recording.interactions[0]

    assert i.http_verb == "GET"
    assert i.path == "/path/to/resource"
    assert str(i.request_headers) == "{'Header1': '11', 'Header2': '22'}"
    assert i.request_body == "abc123"

    assert i.response_type == "text/plain"
    assert i.response_code == "200"
    assert str(i.response_headers) == "{'Content-Type': 'text/plain', 'Header-X': 'abc-123'}"
    assert i.response_body == "Mary had a little lamb"

    i = recording.interactions[1]
    assert i.path == "/path/to/another/thing"
    assert str(i.request_headers) == "{'Its_fleece': 'Was white as snow'}"
    assert i.request_body == "And every where that Mary went"

    assert i.response_type == "nursery/rhyme"
    assert i.response_code == "201"
    assert str(i.response_headers) == "{'Content-Type': 'nursery/rhyme', 'The_lamb': 'was sure to go ;'}"
    assert i.response_body == "He followed her to school one day—"
