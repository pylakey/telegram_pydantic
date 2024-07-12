from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRequestPhone(BaseModel):
    """
    types.KeyboardButtonRequestPhone
    ID: 0xb16a6c29
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRequestPhone', 'KeyboardButtonRequestPhone'] = pydantic.Field(
        'types.KeyboardButtonRequestPhone',
        alias='_'
    )

    text: str
