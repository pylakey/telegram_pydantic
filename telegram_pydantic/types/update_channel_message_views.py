from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelMessageViews(BaseModel):
    """
    types.UpdateChannelMessageViews
    ID: 0xf226ac08
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelMessageViews', 'UpdateChannelMessageViews'] = pydantic.Field(
        'types.UpdateChannelMessageViews',
        alias='_'
    )

    channel_id: int
    id: int
    views: int
