from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityBotCommand(BaseModel):
    """
    types.MessageEntityBotCommand
    ID: 0x6cef8ac7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityBotCommand', 'MessageEntityBotCommand'] = pydantic.Field(
        'types.MessageEntityBotCommand',
        alias='_'
    )

    offset: int
    length: int
