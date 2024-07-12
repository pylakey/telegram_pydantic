from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplyKeyboardMarkup(BaseModel):
    """
    types.ReplyKeyboardMarkup
    ID: 0x85dd99d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReplyKeyboardMarkup', 'ReplyKeyboardMarkup'] = pydantic.Field(
        'types.ReplyKeyboardMarkup',
        alias='_'
    )

    rows: list["base.KeyboardButtonRow"]
    resize: typing.Optional[bool] = None
    single_use: typing.Optional[bool] = None
    selective: typing.Optional[bool] = None
    persistent: typing.Optional[bool] = None
    placeholder: typing.Optional[str] = None
