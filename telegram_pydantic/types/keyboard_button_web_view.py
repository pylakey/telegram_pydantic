from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonWebView(BaseModel):
    """
    types.KeyboardButtonWebView
    ID: 0x13767230
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonWebView', 'KeyboardButtonWebView'] = pydantic.Field(
        'types.KeyboardButtonWebView',
        alias='_'
    )

    text: str
    url: str
