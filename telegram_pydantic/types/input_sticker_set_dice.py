from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetDice(BaseModel):
    """
    types.InputStickerSetDice
    ID: 0xe67f520e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetDice', 'InputStickerSetDice'] = pydantic.Field(
        'types.InputStickerSetDice',
        alias='_'
    )

    emoticon: str
