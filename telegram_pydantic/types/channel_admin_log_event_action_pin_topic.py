from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionPinTopic(BaseModel):
    """
    types.ChannelAdminLogEventActionPinTopic
    ID: 0x5d8d353b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionPinTopic', 'ChannelAdminLogEventActionPinTopic'] = pydantic.Field(
        'types.ChannelAdminLogEventActionPinTopic',
        alias='_'
    )

    prev_topic: typing.Optional["base.ForumTopic"] = None
    new_topic: typing.Optional["base.ForumTopic"] = None
