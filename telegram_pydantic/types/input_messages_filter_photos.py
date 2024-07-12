from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPhotos(BaseModel):
    """
    types.InputMessagesFilterPhotos
    ID: 0x9609a51c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPhotos', 'InputMessagesFilterPhotos'] = pydantic.Field(
        'types.InputMessagesFilterPhotos',
        alias='_'
    )

