from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextBold(BaseModel):
    """
    types.TextBold
    ID: 0x6724abc4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextBold', 'TextBold'] = pydantic.Field(
        'types.TextBold',
        alias='_'
    )

    text: "base.RichText"
