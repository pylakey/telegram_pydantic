from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroupPremium(BaseModel):
    """
    types.EmojiGroupPremium
    ID: 0x93bcf34
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiGroupPremium', 'EmojiGroupPremium'] = pydantic.Field(
        'types.EmojiGroupPremium',
        alias='_'
    )

    title: str
    icon_emoji_id: int
