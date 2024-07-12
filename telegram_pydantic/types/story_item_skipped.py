from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryItemSkipped(BaseModel):
    """
    types.StoryItemSkipped
    ID: 0xffadc913
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryItemSkipped', 'StoryItemSkipped'] = pydantic.Field(
        'types.StoryItemSkipped',
        alias='_'
    )

    id: int
    date: Datetime
    expire_date: Datetime
    close_friends: typing.Optional[bool] = None
