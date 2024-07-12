from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageMediaInvoice(BaseModel):
    """
    types.InputBotInlineMessageMediaInvoice
    ID: 0xd7e78225
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageMediaInvoice', 'InputBotInlineMessageMediaInvoice'] = pydantic.Field(
        'types.InputBotInlineMessageMediaInvoice',
        alias='_'
    )

    title: str
    description: str
    invoice: "base.Invoice"
    payload: Bytes
    provider: str
    provider_data: "base.DataJSON"
    photo: typing.Optional["base.InputWebDocument"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
