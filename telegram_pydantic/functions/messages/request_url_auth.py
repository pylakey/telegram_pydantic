from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestUrlAuth(BaseModel):
    """
    functions.messages.RequestUrlAuth
    ID: 0x198fb446
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RequestUrlAuth', 'RequestUrlAuth'] = pydantic.Field(
        'functions.messages.RequestUrlAuth',
        alias='_'
    )

    peer: typing.Optional["base.InputPeer"] = None
    msg_id: typing.Optional[int] = None
    button_id: typing.Optional[int] = None
    url: typing.Optional[str] = None
