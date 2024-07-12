from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockKicker(BaseModel):
    """
    types.PageBlockKicker
    ID: 0x1e148390
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockKicker', 'PageBlockKicker'] = pydantic.Field(
        'types.PageBlockKicker',
        alias='_'
    )

    text: "base.RichText"
