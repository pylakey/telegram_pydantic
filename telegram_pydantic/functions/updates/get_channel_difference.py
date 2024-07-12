from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelDifference(BaseModel):
    """
    functions.updates.GetChannelDifference
    ID: 0x3173d78
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.updates.GetChannelDifference', 'GetChannelDifference'] = pydantic.Field(
        'functions.updates.GetChannelDifference',
        alias='_'
    )

    channel: "base.InputChannel"
    filter: "base.ChannelMessagesFilter"
    pts: int
    limit: int
    force: typing.Optional[bool] = None
