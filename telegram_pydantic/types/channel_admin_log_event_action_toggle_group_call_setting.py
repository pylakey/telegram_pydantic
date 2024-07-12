from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleGroupCallSetting(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleGroupCallSetting
    ID: 0x56d6a247
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleGroupCallSetting', 'ChannelAdminLogEventActionToggleGroupCallSetting'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleGroupCallSetting',
        alias='_'
    )

    join_muted: bool
