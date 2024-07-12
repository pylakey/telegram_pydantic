from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterEmpty(BaseModel):
    """
    types.InputMessagesFilterEmpty
    ID: 0x57e2f66c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterEmpty', 'InputMessagesFilterEmpty'] = pydantic.Field(
        'types.InputMessagesFilterEmpty',
        alias='_'
    )

