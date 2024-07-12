from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageRelatedArticle(BaseModel):
    """
    types.PageRelatedArticle
    ID: 0xb390dc08
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageRelatedArticle', 'PageRelatedArticle'] = pydantic.Field(
        'types.PageRelatedArticle',
        alias='_'
    )

    url: str
    webpage_id: int
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    photo_id: typing.Optional[int] = None
    author: typing.Optional[str] = None
    published_date: Datetime
