from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityMention(BaseModel):
    """
    types.MessageEntityMention
    ID: 0xfa04579d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityMention', 'MessageEntityMention'] = pydantic.Field(
        'types.MessageEntityMention',
        alias='_'
    )

    offset: int
    length: int
