from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextAnchor(BaseModel):
    """
    types.TextAnchor
    ID: 0x35553762
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextAnchor', 'TextAnchor'] = pydantic.Field(
        'types.TextAnchor',
        alias='_'
    )

    text: "base.RichText"
    name: str
