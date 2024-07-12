from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockPullquote(BaseModel):
    """
    types.PageBlockPullquote
    ID: 0x4f4456d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockPullquote', 'PageBlockPullquote'] = pydantic.Field(
        'types.PageBlockPullquote',
        alias='_'
    )

    text: "base.RichText"
    caption: "base.RichText"
