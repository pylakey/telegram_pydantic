from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebViewResultUrl(BaseModel):
    """
    types.WebViewResultUrl
    ID: 0xc14557c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebViewResultUrl', 'WebViewResultUrl'] = pydantic.Field(
        'types.WebViewResultUrl',
        alias='_'
    )

    query_id: int
    url: str
