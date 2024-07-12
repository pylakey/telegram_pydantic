from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAttachedStickers(BaseModel):
    """
    functions.messages.GetAttachedStickers
    ID: 0xcc5b67cc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAttachedStickers', 'GetAttachedStickers'] = pydantic.Field(
        'functions.messages.GetAttachedStickers',
        alias='_'
    )

    media: "base.InputStickeredMedia"
