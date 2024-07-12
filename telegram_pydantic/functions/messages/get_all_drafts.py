from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAllDrafts(BaseModel):
    """
    functions.messages.GetAllDrafts
    ID: 0x6a3f8d65
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAllDrafts', 'GetAllDrafts'] = pydantic.Field(
        'functions.messages.GetAllDrafts',
        alias='_'
    )

