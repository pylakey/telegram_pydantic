from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeProfilePeerColor(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeProfilePeerColor
    ID: 0x5e477b25
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeProfilePeerColor', 'ChannelAdminLogEventActionChangeProfilePeerColor'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeProfilePeerColor',
        alias='_'
    )

    prev_value: "base.PeerColor"
    new_value: "base.PeerColor"
