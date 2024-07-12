from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateGroupCall(BaseModel):
    """
    functions.phone.CreateGroupCall
    ID: 0x48cdc6d8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.CreateGroupCall', 'CreateGroupCall'] = pydantic.Field(
        'functions.phone.CreateGroupCall',
        alias='_'
    )

    peer: "base.InputPeer"
    random_id: int
    rtmp_stream: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    schedule_date: Datetime
