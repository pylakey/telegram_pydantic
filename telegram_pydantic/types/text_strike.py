from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextStrike(BaseModel):
    """
    types.TextStrike
    ID: 0x9bf8bb95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextStrike', 'TextStrike'] = pydantic.Field(
        'types.TextStrike',
        alias='_'
    )

    text: "base.RichText"
