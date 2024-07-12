from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleNoForwards(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleNoForwards
    ID: 0xcb2ac766
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleNoForwards', 'ChannelAdminLogEventActionToggleNoForwards'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleNoForwards',
        alias='_'
    )

    new_value: bool
