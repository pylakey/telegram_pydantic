from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetOutboxReadDate(BaseModel):
    """
    functions.messages.GetOutboxReadDate
    ID: 0x8c4bfe5d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetOutboxReadDate', 'GetOutboxReadDate'] = pydantic.Field(
        'functions.messages.GetOutboxReadDate',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
