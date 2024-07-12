from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeCall(BaseModel):
    """
    types.auth.SentCodeTypeCall
    ID: 0x5353e5a7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeCall', 'SentCodeTypeCall'] = pydantic.Field(
        'types.auth.SentCodeTypeCall',
        alias='_'
    )

    length: int
