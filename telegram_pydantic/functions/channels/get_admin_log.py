from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAdminLog(BaseModel):
    """
    functions.channels.GetAdminLog
    ID: 0x33ddf480
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetAdminLog', 'GetAdminLog'] = pydantic.Field(
        'functions.channels.GetAdminLog',
        alias='_'
    )

    channel: "base.InputChannel"
    q: str
    max_id: int
    min_id: int
    limit: int
    events_filter: typing.Optional["base.ChannelAdminLogEventsFilter"] = None
    admins: typing.Optional[list["base.InputUser"]] = None
