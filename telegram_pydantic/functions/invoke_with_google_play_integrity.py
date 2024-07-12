from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithGooglePlayIntegrity(BaseModel):
    """
    functions.InvokeWithGooglePlayIntegrity
    ID: 0x1df92984
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithGooglePlayIntegrity', 'InvokeWithGooglePlayIntegrity'] = pydantic.Field(
        'functions.InvokeWithGooglePlayIntegrity',
        alias='_'
    )

    nonce: str
    token: str
    query: BaseModel
