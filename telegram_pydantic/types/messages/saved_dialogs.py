from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedDialogs(BaseModel):
    """
    types.messages.SavedDialogs
    ID: 0xf83ae221
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedDialogs', 'SavedDialogs'] = pydantic.Field(
        'types.messages.SavedDialogs',
        alias='_'
    )

    dialogs: list["base.SavedDialog"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
