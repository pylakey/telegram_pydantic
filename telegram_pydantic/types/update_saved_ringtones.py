from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedRingtones(BaseModel):
    """
    types.UpdateSavedRingtones
    ID: 0x74d8be99
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedRingtones', 'UpdateSavedRingtones'] = pydantic.Field(
        'types.UpdateSavedRingtones',
        alias='_'
    )

