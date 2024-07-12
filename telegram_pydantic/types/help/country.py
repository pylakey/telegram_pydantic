from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Country(BaseModel):
    """
    types.help.Country
    ID: 0xc3878e23
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.Country', 'Country'] = pydantic.Field(
        'types.help.Country',
        alias='_'
    )

    iso2: str
    default_name: str
    country_codes: list["base.help.CountryCode"]
    hidden: typing.Optional[bool] = None
    name: typing.Optional[str] = None
