from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessageEditData(BaseModel):
    """
    functions.messages.GetMessageEditData
    ID: 0xfda68d36
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessageEditData', 'GetMessageEditData'] = pydantic.Field(
        'functions.messages.GetMessageEditData',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
