from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSettings(BaseModel):
    """
    functions.smsjobs.UpdateSettings
    ID: 0x93fa0bf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.UpdateSettings', 'UpdateSettings'] = pydantic.Field(
        'functions.smsjobs.UpdateSettings',
        alias='_'
    )

    allow_international: typing.Optional[bool] = None
