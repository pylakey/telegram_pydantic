from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetNotifySettings(BaseModel):
    """
    functions.account.ResetNotifySettings
    ID: 0xdb7e1747
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetNotifySettings', 'ResetNotifySettings'] = pydantic.Field(
        'functions.account.ResetNotifySettings',
        alias='_'
    )

