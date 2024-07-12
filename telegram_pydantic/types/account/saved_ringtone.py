from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedRingtone(BaseModel):
    """
    types.account.SavedRingtone
    ID: 0xb7263f6d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SavedRingtone', 'SavedRingtone'] = pydantic.Field(
        'types.account.SavedRingtone',
        alias='_'
    )

