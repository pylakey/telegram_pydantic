from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultBackgroundEmojis(BaseModel):
    """
    functions.account.GetDefaultBackgroundEmojis
    ID: 0xa60ab9ce
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultBackgroundEmojis', 'GetDefaultBackgroundEmojis'] = pydantic.Field(
        'functions.account.GetDefaultBackgroundEmojis',
        alias='_'
    )

    hash: int
