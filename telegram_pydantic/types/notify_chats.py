from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyChats(BaseModel):
    """
    types.NotifyChats
    ID: 0xc007cec3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyChats', 'NotifyChats'] = pydantic.Field(
        'types.NotifyChats',
        alias='_'
    )

