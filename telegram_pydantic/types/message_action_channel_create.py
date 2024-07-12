from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChannelCreate(BaseModel):
    """
    types.MessageActionChannelCreate
    ID: 0x95d2ac92
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChannelCreate', 'MessageActionChannelCreate'] = pydantic.Field(
        'types.MessageActionChannelCreate',
        alias='_'
    )

    title: str
