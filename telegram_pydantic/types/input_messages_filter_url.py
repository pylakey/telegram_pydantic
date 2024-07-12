from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterUrl(BaseModel):
    """
    types.InputMessagesFilterUrl
    ID: 0x7ef0dd87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterUrl', 'InputMessagesFilterUrl'] = pydantic.Field(
        'types.InputMessagesFilterUrl',
        alias='_'
    )

