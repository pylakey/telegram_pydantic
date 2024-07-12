from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeFirebaseSms(BaseModel):
    """
    types.auth.SentCodeTypeFirebaseSms
    ID: 0x13c90f17
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeFirebaseSms', 'SentCodeTypeFirebaseSms'] = pydantic.Field(
        'types.auth.SentCodeTypeFirebaseSms',
        alias='_'
    )

    length: int
    nonce: typing.Optional[Bytes] = None
    play_integrity_nonce: typing.Optional[Bytes] = None
    receipt: typing.Optional[str] = None
    push_timeout: typing.Optional[int] = None
