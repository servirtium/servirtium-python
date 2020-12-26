import threading
from unittest.mock import patch

import requests
from servirtium import recorder
from definitions import MOCKS_DIR


@patch('servirtium.recorder.RecorderHttpHandler.perform_request_on_real_service')
def test_something(mock_perform_request_on_real_service):
    mock_perform_request_on_real_service.return_value = AttrDict({
        "status_code": 200,
        "content": str.encode("something wonderful has happened", encoding="utf-8"),
        "headers": {
            "Content-Type": "text/plain",
            "a": "1"
        }
    })
    # servirtium_site = "http://localhost:61417"

    recorder.set_real_service('http://climatedataapi.worldbank.org')
    recorder.set_request_header_replacements({'User-Agent': 'Servirtium-Testing'})
    recorder.set_response_header_removals({'Set-Cookie: AWSALB', 'X-', "Date:"})

    servirtium_daemon = threading.Thread(target=recorder.start, daemon=True)
    servirtium_daemon.start()

    recorder.RecorderHttpHandler.set_markdown_filename("just_testing_ignore_me")

    rsp = requests.get("http://localhost:61417/abc/123")

    assert rsp.content.decode(encoding="utf-8") == "something wonderful has happened"

    recording = open(MOCKS_DIR + "just_testing_ignore_me.md", "r").read()

    assert recording == """## Interaction 0: GET /abc/123

### Request headers recorded for playback:

```
Host: climatedataapi.worldbank.org
User-Agent: Servirtium-Testing
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
```

### Request body recorded for playback ():

```


```

### Response headers recorded for playback:

```
Content-Type: text/plain
a: 1
```

### Response body recorded for playback (200: text/plain):

```
something wonderful has happened
```
"""


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

# curl --location --request POST 'https://postman-echo.com/post' \
# --data-raw 'This is expected to be sent back as part of response body.'
