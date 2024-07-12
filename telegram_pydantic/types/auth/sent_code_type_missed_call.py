from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeMissedCall(BaseModel):
    """
    types.auth.SentCodeTypeMissedCall
    ID: 0x82006484
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeMissedCall', 'SentCodeTypeMissedCall'] = pydantic.Field(
        'types.auth.SentCodeTypeMissedCall',
        alias='_'
    )

    prefix: str
    length: int
