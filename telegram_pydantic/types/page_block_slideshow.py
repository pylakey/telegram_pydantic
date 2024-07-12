from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockSlideshow(BaseModel):
    """
    types.PageBlockSlideshow
    ID: 0x31f9590
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockSlideshow', 'PageBlockSlideshow'] = pydantic.Field(
        'types.PageBlockSlideshow',
        alias='_'
    )

    items: list["base.PageBlock"]
    caption: "base.PageCaption"
