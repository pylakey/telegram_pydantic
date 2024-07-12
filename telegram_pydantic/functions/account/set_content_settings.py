from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetContentSettings(BaseModel):
    """
    functions.account.SetContentSettings
    ID: 0xb574b16b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetContentSettings', 'SetContentSettings'] = pydantic.Field(
        'functions.account.SetContentSettings',
        alias='_'
    )

    sensitive_enabled: typing.Optional[bool] = None
