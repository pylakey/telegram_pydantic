from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionDiscardGroupCall(BaseModel):
    """
    types.ChannelAdminLogEventActionDiscardGroupCall
    ID: 0xdb9f9140
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionDiscardGroupCall', 'ChannelAdminLogEventActionDiscardGroupCall'] = pydantic.Field(
        'types.ChannelAdminLogEventActionDiscardGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
