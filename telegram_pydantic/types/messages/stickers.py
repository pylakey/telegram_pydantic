from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Stickers(BaseModel):
    """
    types.messages.Stickers
    ID: 0x30a6ec7e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.Stickers', 'Stickers'] = pydantic.Field(
        'types.messages.Stickers',
        alias='_'
    )

    hash: int
    stickers: list["base.Document"]
