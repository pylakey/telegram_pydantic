from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaWebPage(BaseModel):
    """
    types.InputMediaWebPage
    ID: 0xc21b8849
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaWebPage', 'InputMediaWebPage'] = pydantic.Field(
        'types.InputMediaWebPage',
        alias='_'
    )

    url: str
    force_large_media: typing.Optional[bool] = None
    force_small_media: typing.Optional[bool] = None
    optional: typing.Optional[bool] = None
