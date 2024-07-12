from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateTheme(BaseModel):
    """
    functions.account.CreateTheme
    ID: 0x652e4400
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.CreateTheme', 'CreateTheme'] = pydantic.Field(
        'functions.account.CreateTheme',
        alias='_'
    )

    slug: str
    title: str
    document: typing.Optional["base.InputDocument"] = None
    settings: typing.Optional[list["base.InputThemeSettings"]] = None
