from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HideChatlistUpdates(BaseModel):
    """
    functions.chatlists.HideChatlistUpdates
    ID: 0x66e486fb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.HideChatlistUpdates', 'HideChatlistUpdates'] = pydantic.Field(
        'functions.chatlists.HideChatlistUpdates',
        alias='_'
    )

    chatlist: "base.InputChatlist"
