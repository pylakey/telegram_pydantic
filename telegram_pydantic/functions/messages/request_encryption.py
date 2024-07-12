from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestEncryption(BaseModel):
    """
    functions.messages.RequestEncryption
    ID: 0xf64daf43
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RequestEncryption', 'RequestEncryption'] = pydantic.Field(
        'functions.messages.RequestEncryption',
        alias='_'
    )

    user_id: "base.InputUser"
    random_id: int
    g_a: Bytes
