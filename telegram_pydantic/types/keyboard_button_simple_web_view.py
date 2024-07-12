from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonSimpleWebView(BaseModel):
    """
    types.KeyboardButtonSimpleWebView
    ID: 0xa0c0505c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonSimpleWebView', 'KeyboardButtonSimpleWebView'] = pydantic.Field(
        'types.KeyboardButtonSimpleWebView',
        alias='_'
    )

    text: str
    url: str
