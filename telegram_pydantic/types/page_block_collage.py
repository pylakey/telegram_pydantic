from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockCollage(BaseModel):
    """
    types.PageBlockCollage
    ID: 0x65a0fa4d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockCollage', 'PageBlockCollage'] = pydantic.Field(
        'types.PageBlockCollage',
        alias='_'
    )

    items: list["base.PageBlock"]
    caption: "base.PageCaption"
