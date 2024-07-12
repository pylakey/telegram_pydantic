from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextSubscript(BaseModel):
    """
    types.TextSubscript
    ID: 0xed6a8504
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextSubscript', 'TextSubscript'] = pydantic.Field(
        'types.TextSubscript',
        alias='_'
    )

    text: "base.RichText"
