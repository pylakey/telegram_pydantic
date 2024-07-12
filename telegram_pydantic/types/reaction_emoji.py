from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionEmoji(BaseModel):
    """
    types.ReactionEmoji
    ID: 0x1b2286b8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionEmoji', 'ReactionEmoji'] = pydantic.Field(
        'types.ReactionEmoji',
        alias='_'
    )

    emoticon: str
