from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroups(BaseModel):
    """
    types.messages.EmojiGroups
    ID: 0x881fb94b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.EmojiGroups', 'EmojiGroups'] = pydantic.Field(
        'types.messages.EmojiGroups',
        alias='_'
    )

    hash: int
    groups: list["base.EmojiGroup"]
