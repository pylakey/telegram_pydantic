from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagePinned(BaseModel):
    """
    types.InputMessagePinned
    ID: 0x86872538
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagePinned', 'InputMessagePinned'] = pydantic.Field(
        'types.InputMessagePinned',
        alias='_'
    )

