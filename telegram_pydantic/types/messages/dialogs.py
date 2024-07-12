from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Dialogs(BaseModel):
    """
    types.messages.Dialogs
    ID: 0x15ba6c40
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.Dialogs', 'Dialogs'] = pydantic.Field(
        'types.messages.Dialogs',
        alias='_'
    )

    dialogs: list["base.Dialog"]
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
