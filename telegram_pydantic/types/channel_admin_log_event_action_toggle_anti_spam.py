from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleAntiSpam(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleAntiSpam
    ID: 0x64f36dfc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleAntiSpam', 'ChannelAdminLogEventActionToggleAntiSpam'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleAntiSpam',
        alias='_'
    )

    new_value: bool
