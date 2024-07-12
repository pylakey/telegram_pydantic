from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDialogFilters(BaseModel):
    """
    functions.messages.GetDialogFilters
    ID: 0xefd48c89
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDialogFilters', 'GetDialogFilters'] = pydantic.Field(
        'functions.messages.GetDialogFilters',
        alias='_'
    )

