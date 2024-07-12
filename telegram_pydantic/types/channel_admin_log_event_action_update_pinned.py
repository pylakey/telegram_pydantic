from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionUpdatePinned(BaseModel):
    """
    types.ChannelAdminLogEventActionUpdatePinned
    ID: 0xe9e82c18
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionUpdatePinned', 'ChannelAdminLogEventActionUpdatePinned'] = pydantic.Field(
        'types.ChannelAdminLogEventActionUpdatePinned',
        alias='_'
    )

    message: "base.Message"
