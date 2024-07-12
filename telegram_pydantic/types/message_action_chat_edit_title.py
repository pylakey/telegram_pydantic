from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatEditTitle(BaseModel):
    """
    types.MessageActionChatEditTitle
    ID: 0xb5a1ce5a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatEditTitle', 'MessageActionChatEditTitle'] = pydantic.Field(
        'types.MessageActionChatEditTitle',
        alias='_'
    )

    title: str
