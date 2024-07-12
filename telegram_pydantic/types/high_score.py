from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HighScore(BaseModel):
    """
    types.HighScore
    ID: 0x73a379eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.HighScore', 'HighScore'] = pydantic.Field(
        'types.HighScore',
        alias='_'
    )

    pos: int
    user_id: int
    score: int
