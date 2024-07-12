from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteChatUser(BaseModel):
    """
    functions.messages.DeleteChatUser
    ID: 0xa2185cab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteChatUser', 'DeleteChatUser'] = pydantic.Field(
        'functions.messages.DeleteChatUser',
        alias='_'
    )

    chat_id: int
    user_id: "base.InputUser"
    revoke_history: typing.Optional[bool] = None
