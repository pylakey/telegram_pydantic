from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroupsNotModified(BaseModel):
    """
    types.messages.EmojiGroupsNotModified
    ID: 0x6fb4ad87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.EmojiGroupsNotModified', 'EmojiGroupsNotModified'] = pydantic.Field(
        'types.messages.EmojiGroupsNotModified',
        alias='_'
    )

