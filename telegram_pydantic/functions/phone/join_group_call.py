from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinGroupCall(BaseModel):
    """
    functions.phone.JoinGroupCall
    ID: 0xb132ff7b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.JoinGroupCall', 'JoinGroupCall'] = pydantic.Field(
        'functions.phone.JoinGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    join_as: "base.InputPeer"
    params: "base.DataJSON"
    muted: typing.Optional[bool] = None
    video_stopped: typing.Optional[bool] = None
    invite_hash: typing.Optional[str] = None
