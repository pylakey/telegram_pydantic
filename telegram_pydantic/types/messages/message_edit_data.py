from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEditData(BaseModel):
    """
    types.messages.MessageEditData
    ID: 0x26b5dde6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MessageEditData', 'MessageEditData'] = pydantic.Field(
        'types.messages.MessageEditData',
        alias='_'
    )

    caption: typing.Optional[bool] = None
