from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPage(BaseModel):
    """
    types.WebPage
    ID: 0xe89c45b2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPage', 'WebPage'] = pydantic.Field(
        'types.WebPage',
        alias='_'
    )

    id: int
    url: str
    display_url: str
    hash: int
    has_large_media: typing.Optional[bool] = None
    type: typing.Optional[str] = None
    site_name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    photo: typing.Optional["base.Photo"] = None
    embed_url: typing.Optional[str] = None
    embed_type: typing.Optional[str] = None
    embed_width: typing.Optional[int] = None
    embed_height: typing.Optional[int] = None
    duration: typing.Optional[int] = None
    author: typing.Optional[str] = None
    document: typing.Optional["base.Document"] = None
    cached_page: typing.Optional["base.Page"] = None
    attributes: typing.Optional[list["base.WebPageAttribute"]] = None
