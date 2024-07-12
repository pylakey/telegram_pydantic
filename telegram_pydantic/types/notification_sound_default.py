from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotificationSoundDefault(BaseModel):
    """
    types.NotificationSoundDefault
    ID: 0x97e8bebe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotificationSoundDefault', 'NotificationSoundDefault'] = pydantic.Field(
        'types.NotificationSoundDefault',
        alias='_'
    )

