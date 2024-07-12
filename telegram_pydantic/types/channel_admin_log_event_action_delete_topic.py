from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionDeleteTopic(BaseModel):
    """
    types.ChannelAdminLogEventActionDeleteTopic
    ID: 0xae168909
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionDeleteTopic', 'ChannelAdminLogEventActionDeleteTopic'] = pydantic.Field(
        'types.ChannelAdminLogEventActionDeleteTopic',
        alias='_'
    )

    topic: "base.ForumTopic"
