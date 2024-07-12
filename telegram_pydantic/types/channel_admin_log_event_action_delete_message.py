from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionDeleteMessage(BaseModel):
    """
    types.ChannelAdminLogEventActionDeleteMessage
    ID: 0x42e047bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionDeleteMessage', 'ChannelAdminLogEventActionDeleteMessage'] = pydantic.Field(
        'types.ChannelAdminLogEventActionDeleteMessage',
        alias='_'
    )

    message: "base.Message"
