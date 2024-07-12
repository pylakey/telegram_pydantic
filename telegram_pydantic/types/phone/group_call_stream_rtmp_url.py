from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallStreamRtmpUrl(BaseModel):
    """
    types.phone.GroupCallStreamRtmpUrl
    ID: 0x2dbf3432
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.GroupCallStreamRtmpUrl', 'GroupCallStreamRtmpUrl'] = pydantic.Field(
        'types.phone.GroupCallStreamRtmpUrl',
        alias='_'
    )

    url: str
    key: str
