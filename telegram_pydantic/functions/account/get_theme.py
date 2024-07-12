from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTheme(BaseModel):
    """
    functions.account.GetTheme
    ID: 0x3a5869ec
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetTheme', 'GetTheme'] = pydantic.Field(
        'functions.account.GetTheme',
        alias='_'
    )

    format: str
    theme: "base.InputTheme"
