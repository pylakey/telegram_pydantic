from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCommonChats(BaseModel):
    """
    functions.messages.GetCommonChats
    ID: 0xe40ca104
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetCommonChats', 'GetCommonChats'] = pydantic.Field(
        'functions.messages.GetCommonChats',
        alias='_'
    )

    user_id: "base.InputUser"
    max_id: int
    limit: int
