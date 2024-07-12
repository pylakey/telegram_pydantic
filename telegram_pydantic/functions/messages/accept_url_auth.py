from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptUrlAuth(BaseModel):
    """
    functions.messages.AcceptUrlAuth
    ID: 0xb12c7125
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.AcceptUrlAuth', 'AcceptUrlAuth'] = pydantic.Field(
        'functions.messages.AcceptUrlAuth',
        alias='_'
    )

    write_allowed: typing.Optional[bool] = None
    peer: typing.Optional["base.InputPeer"] = None
    msg_id: typing.Optional[int] = None
    button_id: typing.Optional[int] = None
    url: typing.Optional[str] = None
