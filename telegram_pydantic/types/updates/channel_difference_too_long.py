from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelDifferenceTooLong(BaseModel):
    """
    types.updates.ChannelDifferenceTooLong
    ID: 0xa4bcc6fe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.ChannelDifferenceTooLong', 'ChannelDifferenceTooLong'] = pydantic.Field(
        'types.updates.ChannelDifferenceTooLong',
        alias='_'
    )

    dialog: "base.Dialog"
    messages: list["base.Message"]
    chats: list["base.Chat"]
    users: list["base.User"]
    final: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None
