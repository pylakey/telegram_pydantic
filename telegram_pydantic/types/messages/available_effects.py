from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableEffects(BaseModel):
    """
    types.messages.AvailableEffects
    ID: 0xbddb616e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AvailableEffects', 'AvailableEffects'] = pydantic.Field(
        'types.messages.AvailableEffects',
        alias='_'
    )

    hash: int
    effects: list["base.AvailableEffect"]
    documents: list["base.Document"]
