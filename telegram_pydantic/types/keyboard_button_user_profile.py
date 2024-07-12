from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonUserProfile(BaseModel):
    """
    types.KeyboardButtonUserProfile
    ID: 0x308660c1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonUserProfile', 'KeyboardButtonUserProfile'] = pydantic.Field(
        'types.KeyboardButtonUserProfile',
        alias='_'
    )

    text: str
    user_id: int
