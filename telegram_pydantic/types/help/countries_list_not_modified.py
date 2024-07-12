from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CountriesListNotModified(BaseModel):
    """
    types.help.CountriesListNotModified
    ID: 0x93cc1f32
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.CountriesListNotModified', 'CountriesListNotModified'] = pydantic.Field(
        'types.help.CountriesListNotModified',
        alias='_'
    )

