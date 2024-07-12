from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChatlistUpdates(BaseModel):
    """
    functions.chatlists.GetChatlistUpdates
    ID: 0x89419521
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.GetChatlistUpdates', 'GetChatlistUpdates'] = pydantic.Field(
        'functions.chatlists.GetChatlistUpdates',
        alias='_'
    )

    chatlist: "base.InputChatlist"
