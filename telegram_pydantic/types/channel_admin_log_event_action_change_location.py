from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeLocation(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeLocation
    ID: 0xe6b76ae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeLocation', 'ChannelAdminLogEventActionChangeLocation'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeLocation',
        alias='_'
    )

    prev_value: "base.ChannelLocation"
    new_value: "base.ChannelLocation"
