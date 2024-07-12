from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelForbidden(BaseModel):
    """
    types.ChannelForbidden
    ID: 0x17d493d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelForbidden', 'ChannelForbidden'] = pydantic.Field(
        'types.ChannelForbidden',
        alias='_'
    )

    id: int
    access_hash: int
    title: str
    broadcast: typing.Optional[bool] = None
    megagroup: typing.Optional[bool] = None
    until_date: Datetime
