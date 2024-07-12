from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportLoginToken(BaseModel):
    """
    functions.auth.ImportLoginToken
    ID: 0x95ac5ce4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ImportLoginToken', 'ImportLoginToken'] = pydantic.Field(
        'functions.auth.ImportLoginToken',
        alias='_'
    )

    token: Bytes
