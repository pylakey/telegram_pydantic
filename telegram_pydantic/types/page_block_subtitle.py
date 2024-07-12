from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockSubtitle(BaseModel):
    """
    types.PageBlockSubtitle
    ID: 0x8ffa9a1f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockSubtitle', 'PageBlockSubtitle'] = pydantic.Field(
        'types.PageBlockSubtitle',
        alias='_'
    )

    text: "base.RichText"
