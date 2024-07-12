from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelWebPage(BaseModel):
    """
    types.UpdateChannelWebPage
    ID: 0x2f2ba99f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelWebPage', 'UpdateChannelWebPage'] = pydantic.Field(
        'types.UpdateChannelWebPage',
        alias='_'
    )

    channel_id: int
    webpage: "base.WebPage"
    pts: int
    pts_count: int
