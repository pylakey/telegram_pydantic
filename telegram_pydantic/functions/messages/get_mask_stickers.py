from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMaskStickers(BaseModel):
    """
    functions.messages.GetMaskStickers
    ID: 0x640f82b8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMaskStickers', 'GetMaskStickers'] = pydantic.Field(
        'functions.messages.GetMaskStickers',
        alias='_'
    )

    hash: int
