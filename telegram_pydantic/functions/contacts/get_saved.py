from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSaved(BaseModel):
    """
    functions.contacts.GetSaved
    ID: 0x82f1e39f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetSaved', 'GetSaved'] = pydantic.Field(
        'functions.contacts.GetSaved',
        alias='_'
    )

