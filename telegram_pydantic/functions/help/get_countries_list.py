from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCountriesList(BaseModel):
    """
    functions.help.GetCountriesList
    ID: 0x735787a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetCountriesList', 'GetCountriesList'] = pydantic.Field(
        'functions.help.GetCountriesList',
        alias='_'
    )

    lang_code: str
    hash: int
