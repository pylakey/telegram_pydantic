from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityBankCard(BaseModel):
    """
    types.MessageEntityBankCard
    ID: 0x761e6af4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityBankCard', 'MessageEntityBankCard'] = pydantic.Field(
        'types.MessageEntityBankCard',
        alias='_'
    )

    offset: int
    length: int
