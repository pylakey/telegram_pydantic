from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SimpleWebViewResultUrl(BaseModel):
    """
    types.SimpleWebViewResultUrl
    ID: 0x882f76bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SimpleWebViewResultUrl', 'SimpleWebViewResultUrl'] = pydantic.Field(
        'types.SimpleWebViewResultUrl',
        alias='_'
    )

    url: str
