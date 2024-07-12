from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelAvailableMessages(BaseModel):
    """
    types.UpdateChannelAvailableMessages
    ID: 0xb23fc698
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelAvailableMessages', 'UpdateChannelAvailableMessages'] = pydantic.Field(
        'types.UpdateChannelAvailableMessages',
        alias='_'
    )

    channel_id: int
    available_min_id: int
