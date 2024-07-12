from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAvailableEffects(BaseModel):
    """
    functions.messages.GetAvailableEffects
    ID: 0xdea20a39
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAvailableEffects', 'GetAvailableEffects'] = pydantic.Field(
        'functions.messages.GetAvailableEffects',
        alias='_'
    )

    hash: int
