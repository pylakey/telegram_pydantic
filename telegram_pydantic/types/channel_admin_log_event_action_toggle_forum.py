from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleForum(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleForum
    ID: 0x2cc6383
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleForum', 'ChannelAdminLogEventActionToggleForum'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleForum',
        alias='_'
    )

    new_value: bool
