from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageMediaGeo(BaseModel):
    """
    types.InputBotInlineMessageMediaGeo
    ID: 0x96929a85
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageMediaGeo', 'InputBotInlineMessageMediaGeo'] = pydantic.Field(
        'types.InputBotInlineMessageMediaGeo',
        alias='_'
    )

    geo_point: "base.InputGeoPoint"
    heading: typing.Optional[int] = None
    period: typing.Optional[int] = None
    proximity_notification_radius: typing.Optional[int] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
