from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SuggestedShortName(BaseModel):
    """
    types.stickers.SuggestedShortName
    ID: 0x85fea03f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stickers.SuggestedShortName', 'SuggestedShortName'] = pydantic.Field(
        'types.stickers.SuggestedShortName',
        alias='_'
    )

    short_name: str
