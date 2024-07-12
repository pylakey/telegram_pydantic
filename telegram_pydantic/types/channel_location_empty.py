from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelLocationEmpty(BaseModel):
    """
    types.ChannelLocationEmpty
    ID: 0xbfb5ad8b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelLocationEmpty', 'ChannelLocationEmpty'] = pydantic.Field(
        'types.ChannelLocationEmpty',
        alias='_'
    )

