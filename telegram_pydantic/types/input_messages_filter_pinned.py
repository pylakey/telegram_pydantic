from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPinned(BaseModel):
    """
    types.InputMessagesFilterPinned
    ID: 0x1bb00451
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPinned', 'InputMessagesFilterPinned'] = pydantic.Field(
        'types.InputMessagesFilterPinned',
        alias='_'
    )

