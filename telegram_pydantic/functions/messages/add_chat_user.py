from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AddChatUser(BaseModel):
    """
    functions.messages.AddChatUser
    ID: 0xcbc6d107
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.AddChatUser', 'AddChatUser'] = pydantic.Field(
        'functions.messages.AddChatUser',
        alias='_'
    )

    chat_id: int
    user_id: "base.InputUser"
    fwd_limit: int
