from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageMediaInvoice(BaseModel):
    """
    types.BotInlineMessageMediaInvoice
    ID: 0x354a9b09
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageMediaInvoice', 'BotInlineMessageMediaInvoice'] = pydantic.Field(
        'types.BotInlineMessageMediaInvoice',
        alias='_'
    )

    title: str
    description: str
    currency: str
    total_amount: int
    shipping_address_requested: typing.Optional[bool] = None
    test: typing.Optional[bool] = None
    photo: typing.Optional["base.WebDocument"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
