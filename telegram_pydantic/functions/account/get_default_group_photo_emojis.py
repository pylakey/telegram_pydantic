from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultGroupPhotoEmojis(BaseModel):
    """
    functions.account.GetDefaultGroupPhotoEmojis
    ID: 0x915860ae
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultGroupPhotoEmojis', 'GetDefaultGroupPhotoEmojis'] = pydantic.Field(
        'functions.account.GetDefaultGroupPhotoEmojis',
        alias='_'
    )

    hash: int
