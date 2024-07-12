from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionBoostApply(BaseModel):
    """
    types.MessageActionBoostApply
    ID: 0xcc02aa6d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionBoostApply', 'MessageActionBoostApply'] = pydantic.Field(
        'types.MessageActionBoostApply',
        alias='_'
    )

    boosts: int
