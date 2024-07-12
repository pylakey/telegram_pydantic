from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityMentionName(BaseModel):
    """
    types.MessageEntityMentionName
    ID: 0xdc7b1140
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityMentionName', 'MessageEntityMentionName'] = pydantic.Field(
        'types.MessageEntityMentionName',
        alias='_'
    )

    offset: int
    length: int
    user_id: int
