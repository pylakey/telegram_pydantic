from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class QuickReply(BaseModel):
    """
    types.QuickReply
    ID: 0x697102b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.QuickReply', 'QuickReply'] = pydantic.Field(
        'types.QuickReply',
        alias='_'
    )

    shortcut_id: int
    shortcut: str
    top_message: int
    count: int
