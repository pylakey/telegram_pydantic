from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CountryCode(BaseModel):
    """
    types.help.CountryCode
    ID: 0x4203c5ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.CountryCode', 'CountryCode'] = pydantic.Field(
        'types.help.CountryCode',
        alias='_'
    )

    country_code: str
    prefixes: typing.Optional[list[str]] = None
    patterns: typing.Optional[list[str]] = None
