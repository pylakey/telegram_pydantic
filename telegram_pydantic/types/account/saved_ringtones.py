from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedRingtones(BaseModel):
    """
    types.account.SavedRingtones
    ID: 0xc1e92cc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SavedRingtones', 'SavedRingtones'] = pydantic.Field(
        'types.account.SavedRingtones',
        alias='_'
    )

    hash: int
    ringtones: list["base.Document"]
