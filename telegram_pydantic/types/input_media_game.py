from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaGame(BaseModel):
    """
    types.InputMediaGame
    ID: 0xd33f43f3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaGame', 'InputMediaGame'] = pydantic.Field(
        'types.InputMediaGame',
        alias='_'
    )

    id: "base.InputGame"
