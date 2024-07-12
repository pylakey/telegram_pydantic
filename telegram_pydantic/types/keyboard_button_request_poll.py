from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRequestPoll(BaseModel):
    """
    types.KeyboardButtonRequestPoll
    ID: 0xbbc7515d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRequestPoll', 'KeyboardButtonRequestPoll'] = pydantic.Field(
        'types.KeyboardButtonRequestPoll',
        alias='_'
    )

    text: str
    quiz: typing.Optional[bool] = None
