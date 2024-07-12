from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedRingtoneConverted(BaseModel):
    """
    types.account.SavedRingtoneConverted
    ID: 0x1f307eb7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SavedRingtoneConverted', 'SavedRingtoneConverted'] = pydantic.Field(
        'types.account.SavedRingtoneConverted',
        alias='_'
    )

    document: "base.Document"
