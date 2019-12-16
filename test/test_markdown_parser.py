import json
import os
import pytest
from unittest.mock import patch

from servirtium.markdown_parser import SimpleMarkdownParser


class TestMarkdownParser:

    if __name__ == "__main__":
        try:
            pytest.main(["-x", os.getcwd()+"/test_markdown_parser.py"])
        finally:
            os._exit(1)

    def test_something(self):

        @patch('SimpleMarkdownParser.get_file_content')
        def test(mock_get_file_content):
            mock_get_file_content.return_value = 'abc 123'
            recording = SimpleMarkdownParser().get_recording_from_method_name("foo")
            print(json.dumps(recording))
            pytest.fail("oops")

