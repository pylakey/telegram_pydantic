from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageCaption(BaseModel):
    """
    types.PageCaption
    ID: 0x6f747657
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageCaption', 'PageCaption'] = pydantic.Field(
        'types.PageCaption',
        alias='_'
    )

    text: "base.RichText"
    credit: "base.RichText"
