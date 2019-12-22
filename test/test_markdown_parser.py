import json
import pytest
from unittest.mock import patch

from markdown_parser import SimpleMarkdownParser


@patch('markdown_parser.SimpleMarkdownParser.get_file_content')
def test_bad_markdown_means_no_recordings(mock_get_file_content):
    mock_get_file_content.return_value = 'abc 123'
    recording = SimpleMarkdownParser().get_recording_from_method_name("foo")
    assert recording is None\

def test_good_markdown_means_recording():
    parser = SimpleMarkdownParser()
    files = parser.get_markdown_file_strings("./test/mocks1")
    parser._set_mock_files(files)
    recording = parser.get_recording_from_method_name("foo")

    assert recording is not None
    assert len(recording.interactions) is 2

    i = recording.interactions[0]
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
