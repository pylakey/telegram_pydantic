from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSmsWord(BaseModel):
    """
    types.auth.SentCodeTypeSmsWord
    ID: 0xa416ac81
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSmsWord', 'SentCodeTypeSmsWord'] = pydantic.Field(
        'types.auth.SentCodeTypeSmsWord',
        alias='_'
    )

    beginning: typing.Optional[str] = None
