from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetThemes(BaseModel):
    """
    functions.account.GetThemes
    ID: 0x7206e458
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetThemes', 'GetThemes'] = pydantic.Field(
        'functions.account.GetThemes',
        alias='_'
    )

    format: str
    hash: int
