from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRow(BaseModel):
    """
    types.KeyboardButtonRow
    ID: 0x77608b83
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRow', 'KeyboardButtonRow'] = pydantic.Field(
        'types.KeyboardButtonRow',
        alias='_'
    )

    buttons: list["base.KeyboardButton"]
