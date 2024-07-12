from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CountriesList(BaseModel):
    """
    types.help.CountriesList
    ID: 0x87d0759e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.CountriesList', 'CountriesList'] = pydantic.Field(
        'types.help.CountriesList',
        alias='_'
    )

    countries: list["base.help.Country"]
    hash: int
