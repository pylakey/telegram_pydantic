from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HighScores(BaseModel):
    """
    types.messages.HighScores
    ID: 0x9a3bfd99
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.HighScores', 'HighScores'] = pydantic.Field(
        'types.messages.HighScores',
        alias='_'
    )

    scores: list["base.HighScore"]
    users: list["base.User"]
