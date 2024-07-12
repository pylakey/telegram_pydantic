from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockVideo(BaseModel):
    """
    types.PageBlockVideo
    ID: 0x7c8fe7b6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockVideo', 'PageBlockVideo'] = pydantic.Field(
        'types.PageBlockVideo',
        alias='_'
    )

    video_id: int
    caption: "base.PageCaption"
    autoplay: typing.Optional[bool] = None
    loop: typing.Optional[bool] = None
