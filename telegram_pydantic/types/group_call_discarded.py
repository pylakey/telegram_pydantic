from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallDiscarded(BaseModel):
    """
    types.GroupCallDiscarded
    ID: 0x7780bcb4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallDiscarded', 'GroupCallDiscarded'] = pydantic.Field(
        'types.GroupCallDiscarded',
        alias='_'
    )

    id: int
    access_hash: int
    duration: int
