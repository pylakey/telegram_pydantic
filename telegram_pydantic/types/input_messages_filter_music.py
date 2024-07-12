from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterMusic(BaseModel):
    """
    types.InputMessagesFilterMusic
    ID: 0x3751b49e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterMusic', 'InputMessagesFilterMusic'] = pydantic.Field(
        'types.InputMessagesFilterMusic',
        alias='_'
    )

