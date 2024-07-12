from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockEmbedPost(BaseModel):
    """
    types.PageBlockEmbedPost
    ID: 0xf259a80b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockEmbedPost', 'PageBlockEmbedPost'] = pydantic.Field(
        'types.PageBlockEmbedPost',
        alias='_'
    )

    url: str
    webpage_id: int
    author_photo_id: int
    author: str
    date: Datetime
    blocks: list["base.PageBlock"]
    caption: "base.PageCaption"
