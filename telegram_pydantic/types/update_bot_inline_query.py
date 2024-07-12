from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotInlineQuery(BaseModel):
    """
    types.UpdateBotInlineQuery
    ID: 0x496f379c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotInlineQuery', 'UpdateBotInlineQuery'] = pydantic.Field(
        'types.UpdateBotInlineQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    query: str
    offset: str
    geo: typing.Optional["base.GeoPoint"] = None
    peer_type: typing.Optional["base.InlineQueryPeerType"] = None
