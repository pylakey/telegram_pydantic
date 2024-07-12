from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockEmbed(BaseModel):
    """
    types.PageBlockEmbed
    ID: 0xa8718dc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockEmbed', 'PageBlockEmbed'] = pydantic.Field(
        'types.PageBlockEmbed',
        alias='_'
    )

    caption: "base.PageCaption"
    full_width: typing.Optional[bool] = None
    allow_scrolling: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    html: typing.Optional[str] = None
    poster_photo_id: typing.Optional[int] = None
    w: typing.Optional[int] = None
    h: typing.Optional[int] = None
