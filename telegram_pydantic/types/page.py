from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Page(BaseModel):
    """
    types.Page
    ID: 0x98657f0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Page', 'Page'] = pydantic.Field(
        'types.Page',
        alias='_'
    )

    url: str
    blocks: list["base.PageBlock"]
    photos: list["base.Photo"]
    documents: list["base.Document"]
    part: typing.Optional[bool] = None
    rtl: typing.Optional[bool] = None
    v2: typing.Optional[bool] = None
    views: typing.Optional[int] = None
