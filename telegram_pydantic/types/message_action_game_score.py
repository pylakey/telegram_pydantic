from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGameScore(BaseModel):
    """
    types.MessageActionGameScore
    ID: 0x92a72876
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGameScore', 'MessageActionGameScore'] = pydantic.Field(
        'types.MessageActionGameScore',
        alias='_'
    )

    game_id: int
    score: int
