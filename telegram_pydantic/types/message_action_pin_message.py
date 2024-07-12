from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionPinMessage(BaseModel):
    """
    types.MessageActionPinMessage
    ID: 0x94bd38ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionPinMessage', 'MessageActionPinMessage'] = pydantic.Field(
        'types.MessageActionPinMessage',
        alias='_'
    )

