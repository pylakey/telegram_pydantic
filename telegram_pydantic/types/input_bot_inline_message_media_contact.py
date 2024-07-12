from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageMediaContact(BaseModel):
    """
    types.InputBotInlineMessageMediaContact
    ID: 0xa6edbffd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageMediaContact', 'InputBotInlineMessageMediaContact'] = pydantic.Field(
        'types.InputBotInlineMessageMediaContact',
        alias='_'
    )

    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
