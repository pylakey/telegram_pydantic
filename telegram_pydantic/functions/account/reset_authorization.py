from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetAuthorization(BaseModel):
    """
    functions.account.ResetAuthorization
    ID: 0xdf77f3bc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetAuthorization', 'ResetAuthorization'] = pydantic.Field(
        'functions.account.ResetAuthorization',
        alias='_'
    )

    hash: int
