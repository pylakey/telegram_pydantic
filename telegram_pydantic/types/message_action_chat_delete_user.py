from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatDeleteUser(BaseModel):
    """
    types.MessageActionChatDeleteUser
    ID: 0xa43f30cc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatDeleteUser', 'MessageActionChatDeleteUser'] = pydantic.Field(
        'types.MessageActionChatDeleteUser',
        alias='_'
    )

    user_id: int
