from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeAvailableReactions(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeAvailableReactions
    ID: 0xbe4e0ef8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeAvailableReactions', 'ChannelAdminLogEventActionChangeAvailableReactions'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeAvailableReactions',
        alias='_'
    )

    prev_value: "base.ChatReactions"
    new_value: "base.ChatReactions"
