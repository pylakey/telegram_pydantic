from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextUrl(BaseModel):
    """
    types.TextUrl
    ID: 0x3c2884c1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextUrl', 'TextUrl'] = pydantic.Field(
        'types.TextUrl',
        alias='_'
    )

    text: "base.RichText"
    url: str
    webpage_id: int
