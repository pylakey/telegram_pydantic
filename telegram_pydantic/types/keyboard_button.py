from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButton(BaseModel):
    """
    types.KeyboardButton
    ID: 0xa2fa4880
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButton', 'KeyboardButton'] = pydantic.Field(
        'types.KeyboardButton',
        alias='_'
    )

    text: str
