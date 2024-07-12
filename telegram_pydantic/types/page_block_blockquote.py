from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockBlockquote(BaseModel):
    """
    types.PageBlockBlockquote
    ID: 0x263d7c26
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockBlockquote', 'PageBlockBlockquote'] = pydantic.Field(
        'types.PageBlockBlockquote',
        alias='_'
    )

    text: "base.RichText"
    caption: "base.RichText"
