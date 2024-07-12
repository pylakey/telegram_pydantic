from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeLinkedChat(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeLinkedChat
    ID: 0x50c7ac8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeLinkedChat', 'ChannelAdminLogEventActionChangeLinkedChat'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeLinkedChat',
        alias='_'
    )

    prev_value: int
    new_value: int
