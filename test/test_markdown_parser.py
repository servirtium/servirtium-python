import json
import pytest
from unittest.mock import patch

from markdown_parser import SimpleMarkdownParser


@patch('markdown_parser.SimpleMarkdownParser.get_file_content')
def test_bad_mrkdown_means_no_recordings(mock_get_file_content):
    mock_get_file_content.return_value = 'abc 123'
    recording = SimpleMarkdownParser().get_recording_from_method_name("foo")
    assert recording is None