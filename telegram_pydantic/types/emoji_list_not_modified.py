from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiListNotModified(BaseModel):
    """
    types.EmojiListNotModified
    ID: 0x481eadfa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiListNotModified', 'EmojiListNotModified'] = pydantic.Field(
        'types.EmojiListNotModified',
        alias='_'
    )

