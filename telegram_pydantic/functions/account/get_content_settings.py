from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetContentSettings(BaseModel):
    """
    functions.account.GetContentSettings
    ID: 0x8b9b4dae
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetContentSettings', 'GetContentSettings'] = pydantic.Field(
        'functions.account.GetContentSettings',
        alias='_'
    )

