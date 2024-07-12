from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatMigrateTo(BaseModel):
    """
    types.MessageActionChatMigrateTo
    ID: 0xe1037f92
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatMigrateTo', 'MessageActionChatMigrateTo'] = pydantic.Field(
        'types.MessageActionChatMigrateTo',
        alias='_'
    )

    channel_id: int
