from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBusinessChatLinks(BaseModel):
    """
    functions.account.GetBusinessChatLinks
    ID: 0x6f70dde1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetBusinessChatLinks', 'GetBusinessChatLinks'] = pydantic.Field(
        'functions.account.GetBusinessChatLinks',
        alias='_'
    )

