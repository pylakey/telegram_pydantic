from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterGif(BaseModel):
    """
    types.InputMessagesFilterGif
    ID: 0xffc86587
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterGif', 'InputMessagesFilterGif'] = pydantic.Field(
        'types.InputMessagesFilterGif',
        alias='_'
    )

