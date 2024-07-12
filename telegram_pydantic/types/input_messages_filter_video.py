from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterVideo(BaseModel):
    """
    types.InputMessagesFilterVideo
    ID: 0x9fc00e65
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterVideo', 'InputMessagesFilterVideo'] = pydantic.Field(
        'types.InputMessagesFilterVideo',
        alias='_'
    )

