from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockRelatedArticles(BaseModel):
    """
    types.PageBlockRelatedArticles
    ID: 0x16115a96
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockRelatedArticles', 'PageBlockRelatedArticles'] = pydantic.Field(
        'types.PageBlockRelatedArticles',
        alias='_'
    )

    title: "base.RichText"
    articles: list["base.PageRelatedArticle"]
