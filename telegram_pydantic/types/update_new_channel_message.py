from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewChannelMessage(BaseModel):
    """
    types.UpdateNewChannelMessage
    ID: 0x62ba04d9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewChannelMessage', 'UpdateNewChannelMessage'] = pydantic.Field(
        'types.UpdateNewChannelMessage',
        alias='_'
    )

    message: "base.Message"
    pts: int
    pts_count: int
