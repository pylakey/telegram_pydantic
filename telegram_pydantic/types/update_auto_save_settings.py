from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateAutoSaveSettings(BaseModel):
    """
    types.UpdateAutoSaveSettings
    ID: 0xec05b097
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateAutoSaveSettings', 'UpdateAutoSaveSettings'] = pydantic.Field(
        'types.UpdateAutoSaveSettings',
        alias='_'
    )

