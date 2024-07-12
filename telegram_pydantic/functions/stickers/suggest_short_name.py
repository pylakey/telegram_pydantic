from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SuggestShortName(BaseModel):
    """
    functions.stickers.SuggestShortName
    ID: 0x4dafc503
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stickers.SuggestShortName', 'SuggestShortName'] = pydantic.Field(
        'functions.stickers.SuggestShortName',
        alias='_'
    )

    title: str
