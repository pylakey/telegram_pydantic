from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeBotPM(BaseModel):
    """
    types.InlineQueryPeerTypeBotPM
    ID: 0xe3b2d0c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeBotPM', 'InlineQueryPeerTypeBotPM'] = pydantic.Field(
        'types.InlineQueryPeerTypeBotPM',
        alias='_'
    )

