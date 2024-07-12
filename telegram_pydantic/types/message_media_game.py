from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaGame(BaseModel):
    """
    types.MessageMediaGame
    ID: 0xfdb19008
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaGame', 'MessageMediaGame'] = pydantic.Field(
        'types.MessageMediaGame',
        alias='_'
    )

    game: "base.Game"
