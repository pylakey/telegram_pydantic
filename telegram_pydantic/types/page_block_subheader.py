from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockSubheader(BaseModel):
    """
    types.PageBlockSubheader
    ID: 0xf12bb6e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockSubheader', 'PageBlockSubheader'] = pydantic.Field(
        'types.PageBlockSubheader',
        alias='_'
    )

    text: "base.RichText"
