from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelMessageForwards(BaseModel):
    """
    types.UpdateChannelMessageForwards
    ID: 0xd29a27f4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelMessageForwards', 'UpdateChannelMessageForwards'] = pydantic.Field(
        'types.UpdateChannelMessageForwards',
        alias='_'
    )

    channel_id: int
    id: int
    forwards: int
