from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockCover(BaseModel):
    """
    types.PageBlockCover
    ID: 0x39f23300
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockCover', 'PageBlockCover'] = pydantic.Field(
        'types.PageBlockCover',
        alias='_'
    )

    cover: "base.PageBlock"
