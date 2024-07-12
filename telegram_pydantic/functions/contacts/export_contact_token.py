from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportContactToken(BaseModel):
    """
    functions.contacts.ExportContactToken
    ID: 0xf8654027
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ExportContactToken', 'ExportContactToken'] = pydantic.Field(
        'functions.contacts.ExportContactToken',
        alias='_'
    )

