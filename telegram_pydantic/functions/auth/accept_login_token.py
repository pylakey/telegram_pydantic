from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptLoginToken(BaseModel):
    """
    functions.auth.AcceptLoginToken
    ID: 0xe894ad4d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.AcceptLoginToken', 'AcceptLoginToken'] = pydantic.Field(
        'functions.auth.AcceptLoginToken',
        alias='_'
    )

    token: Bytes
