from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPassportConfig(BaseModel):
    """
    functions.help.GetPassportConfig
    ID: 0xc661ad08
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPassportConfig', 'GetPassportConfig'] = pydantic.Field(
        'functions.help.GetPassportConfig',
        alias='_'
    )

    hash: int
