from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestFirebaseSms(BaseModel):
    """
    functions.auth.RequestFirebaseSms
    ID: 0x8e39261e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.RequestFirebaseSms', 'RequestFirebaseSms'] = pydantic.Field(
        'functions.auth.RequestFirebaseSms',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    safety_net_token: typing.Optional[str] = None
    play_integrity_token: typing.Optional[str] = None
    ios_push_secret: typing.Optional[str] = None
