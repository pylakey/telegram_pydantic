from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelMessagesFilterEmpty(BaseModel):
    """
    types.ChannelMessagesFilterEmpty
    ID: 0x94d42ee7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelMessagesFilterEmpty', 'ChannelMessagesFilterEmpty'] = pydantic.Field(
        'types.ChannelMessagesFilterEmpty',
        alias='_'
    )

