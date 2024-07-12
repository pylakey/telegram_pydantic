from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterDocument(BaseModel):
    """
    types.InputMessagesFilterDocument
    ID: 0x9eddf188
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterDocument', 'InputMessagesFilterDocument'] = pydantic.Field(
        'types.InputMessagesFilterDocument',
        alias='_'
    )

