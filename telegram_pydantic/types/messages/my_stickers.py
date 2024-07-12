from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MyStickers(BaseModel):
    """
    types.messages.MyStickers
    ID: 0xfaff629d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MyStickers', 'MyStickers'] = pydantic.Field(
        'types.messages.MyStickers',
        alias='_'
    )

    count: int
    sets: list["base.StickerSetCovered"]
