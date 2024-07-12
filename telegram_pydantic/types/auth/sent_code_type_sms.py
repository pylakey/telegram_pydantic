from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSms(BaseModel):
    """
    types.auth.SentCodeTypeSms
    ID: 0xc000bba2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSms', 'SentCodeTypeSms'] = pydantic.Field(
        'types.auth.SentCodeTypeSms',
        alias='_'
    )

    length: int
