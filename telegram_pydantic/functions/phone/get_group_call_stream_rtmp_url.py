from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupCallStreamRtmpUrl(BaseModel):
    """
    functions.phone.GetGroupCallStreamRtmpUrl
    ID: 0xdeb3abbf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupCallStreamRtmpUrl', 'GetGroupCallStreamRtmpUrl'] = pydantic.Field(
        'functions.phone.GetGroupCallStreamRtmpUrl',
        alias='_'
    )

    peer: "base.InputPeer"
    revoke: bool
