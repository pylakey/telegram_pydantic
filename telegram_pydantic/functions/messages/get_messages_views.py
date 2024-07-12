from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessagesViews(BaseModel):
    """
    functions.messages.GetMessagesViews
    ID: 0x5784d3e1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessagesViews', 'GetMessagesViews'] = pydantic.Field(
        'functions.messages.GetMessagesViews',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
    increment: bool
