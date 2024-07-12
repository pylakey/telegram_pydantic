from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageMediaVenue(BaseModel):
    """
    types.BotInlineMessageMediaVenue
    ID: 0x8a86659c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageMediaVenue', 'BotInlineMessageMediaVenue'] = pydantic.Field(
        'types.BotInlineMessageMediaVenue',
        alias='_'
    )

    geo: "base.GeoPoint"
    title: str
    address: str
    provider: str
    venue_id: str
    venue_type: str
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
