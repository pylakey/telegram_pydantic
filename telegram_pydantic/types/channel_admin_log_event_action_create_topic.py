from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionCreateTopic(BaseModel):
    """
    types.ChannelAdminLogEventActionCreateTopic
    ID: 0x58707d28
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionCreateTopic', 'ChannelAdminLogEventActionCreateTopic'] = pydantic.Field(
        'types.ChannelAdminLogEventActionCreateTopic',
        alias='_'
    )

    topic: "base.ForumTopic"
