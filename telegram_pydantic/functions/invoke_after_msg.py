from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeAfterMsg(BaseModel):
    """
    functions.InvokeAfterMsg
    ID: 0xcb9f372d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeAfterMsg', 'InvokeAfterMsg'] = pydantic.Field(
        'functions.InvokeAfterMsg',
        alias='_'
    )

    msg_id: int
    query: BaseModel
