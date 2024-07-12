from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateRecentEmojiStatuses(BaseModel):
    """
    types.UpdateRecentEmojiStatuses
    ID: 0x30f443db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateRecentEmojiStatuses', 'UpdateRecentEmojiStatuses'] = pydantic.Field(
        'types.UpdateRecentEmojiStatuses',
        alias='_'
    )

