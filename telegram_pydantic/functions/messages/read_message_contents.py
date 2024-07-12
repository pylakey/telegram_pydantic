from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadMessageContents(BaseModel):
    """
    functions.messages.ReadMessageContents
    ID: 0x36a73f77
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadMessageContents', 'ReadMessageContents'] = pydantic.Field(
        'functions.messages.ReadMessageContents',
        alias='_'
    )

    id: list[int]
