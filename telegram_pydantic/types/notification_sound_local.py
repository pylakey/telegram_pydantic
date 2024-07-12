from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotificationSoundLocal(BaseModel):
    """
    types.NotificationSoundLocal
    ID: 0x830b9ae4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotificationSoundLocal', 'NotificationSoundLocal'] = pydantic.Field(
        'types.NotificationSoundLocal',
        alias='_'
    )

    title: str
    data: str
