from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockHeader(BaseModel):
    """
    types.PageBlockHeader
    ID: 0xbfd064ec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockHeader', 'PageBlockHeader'] = pydantic.Field(
        'types.PageBlockHeader',
        alias='_'
    )

    text: "base.RichText"
