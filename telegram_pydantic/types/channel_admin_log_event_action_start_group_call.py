from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionStartGroupCall(BaseModel):
    """
    types.ChannelAdminLogEventActionStartGroupCall
    ID: 0x23209745
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionStartGroupCall', 'ChannelAdminLogEventActionStartGroupCall'] = pydantic.Field(
        'types.ChannelAdminLogEventActionStartGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
