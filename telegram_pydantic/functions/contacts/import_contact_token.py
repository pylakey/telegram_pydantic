from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportContactToken(BaseModel):
    """
    functions.contacts.ImportContactToken
    ID: 0x13005788
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ImportContactToken', 'ImportContactToken'] = pydantic.Field(
        'functions.contacts.ImportContactToken',
        alias='_'
    )

    token: str
