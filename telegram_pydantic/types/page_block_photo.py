from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockPhoto(BaseModel):
    """
    types.PageBlockPhoto
    ID: 0x1759c560
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockPhoto', 'PageBlockPhoto'] = pydantic.Field(
        'types.PageBlockPhoto',
        alias='_'
    )

    photo_id: int
    caption: "base.PageCaption"
    url: typing.Optional[str] = None
    webpage_id: typing.Optional[int] = None
