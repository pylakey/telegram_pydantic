from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChannelMigrateFrom(BaseModel):
    """
    types.MessageActionChannelMigrateFrom
    ID: 0xea3948e9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChannelMigrateFrom', 'MessageActionChannelMigrateFrom'] = pydantic.Field(
        'types.MessageActionChannelMigrateFrom',
        alias='_'
    )

    title: str
    chat_id: int
