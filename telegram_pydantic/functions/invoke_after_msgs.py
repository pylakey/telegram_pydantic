from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeAfterMsgs(BaseModel):
    """
    functions.InvokeAfterMsgs
    ID: 0x3dc4b4f0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeAfterMsgs', 'InvokeAfterMsgs'] = pydantic.Field(
        'functions.InvokeAfterMsgs',
        alias='_'
    )

    msg_ids: list[int]
    query: BaseModel
