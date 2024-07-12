from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterChatPhotos(BaseModel):
    """
    types.InputMessagesFilterChatPhotos
    ID: 0x3a20ecb8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterChatPhotos', 'InputMessagesFilterChatPhotos'] = pydantic.Field(
        'types.InputMessagesFilterChatPhotos',
        alias='_'
    )

