from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageMediaGeo(BaseModel):
    """
    types.BotInlineMessageMediaGeo
    ID: 0x51846fd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageMediaGeo', 'BotInlineMessageMediaGeo'] = pydantic.Field(
        'types.BotInlineMessageMediaGeo',
        alias='_'
    )

    geo: "base.GeoPoint"
    heading: typing.Optional[int] = None
    period: typing.Optional[int] = None
    proximity_notification_radius: typing.Optional[int] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
