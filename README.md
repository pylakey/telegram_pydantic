# telegram_pydantic - Set of Pydantic models, generated according to Telegram TL Scheme

[![PyPI version shields.io](https://img.shields.io/pypi/v/telegram_pydantic.svg)](https://pypi.python.org/pypi/telegram_pydantic/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/telegram_pydantic.svg)](https://pypi.python.org/pypi/telegram_pydantic/)
[![PyPI license](https://img.shields.io/pypi/l/telegram_pydantic.svg)](https://pypi.python.org/pypi/telegram_pydantic/)

> Layer 181

## Example

```python
from pydantic import TypeAdapter

from telegram_pydantic import base
from telegram_pydantic import types

ta = TypeAdapter(base.Message)  # Base Constructor

json_data = {
    "_": "types.Message",
    "id": 1,
    "peer_id": {"_": "types.PeerUser", "user_id": 1},
    "date": 1720715931,
    "message": "Hello, World!",
    "out": False,
    "mentioned": False,
    "media_unread": False,
    "silent": False,
    "post": False,
    "from_scheduled": False,
    "legacy": False,
    "edit_hide": False,
    "pinned": False,
    "noforwards": False,
    "invert_media": False,
    "offline": False,
    "saved_peer_id": {"_": "types.PeerUser", "user_id": 1},
    "entities": [],
    "restriction_reason": []
}

message = ta.validate_python(json_data)

print(isinstance(message, types.Message))  # True 

```


## LICENSE

This project is licensed under the terms of the MIT license.
