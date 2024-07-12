from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockMap(BaseModel):
    """
    types.PageBlockMap
    ID: 0xa44f3ef6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockMap', 'PageBlockMap'] = pydantic.Field(
        'types.PageBlockMap',
        alias='_'
    )

    geo: "base.GeoPoint"
    zoom: int
    w: int
    h: int
    caption: "base.PageCaption"
