from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteFactCheck(BaseModel):
    """
    functions.messages.DeleteFactCheck
    ID: 0xd1da940c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteFactCheck', 'DeleteFactCheck'] = pydantic.Field(
        'functions.messages.DeleteFactCheck',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
