from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextItalic(BaseModel):
    """
    types.TextItalic
    ID: 0xd912a59c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextItalic', 'TextItalic'] = pydantic.Field(
        'types.TextItalic',
        alias='_'
    )

    text: "base.RichText"
