from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendWebViewResultMessage(BaseModel):
    """
    functions.messages.SendWebViewResultMessage
    ID: 0xa4314f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendWebViewResultMessage', 'SendWebViewResultMessage'] = pydantic.Field(
        'functions.messages.SendWebViewResultMessage',
        alias='_'
    )

    bot_query_id: str
    result: "base.InputBotInlineResult"
