from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleInvites(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleInvites
    ID: 0x1b7907ae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleInvites', 'ChannelAdminLogEventActionToggleInvites'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleInvites',
        alias='_'
    )

    new_value: bool
