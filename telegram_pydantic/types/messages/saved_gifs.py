from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedGifs(BaseModel):
    """
    types.messages.SavedGifs
    ID: 0x84a02a0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedGifs', 'SavedGifs'] = pydantic.Field(
        'types.messages.SavedGifs',
        alias='_'
    )

    hash: int
    gifs: list["base.Document"]
