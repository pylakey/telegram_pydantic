from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatDeletePhoto(BaseModel):
    """
    types.MessageActionChatDeletePhoto
    ID: 0x95e3fbef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatDeletePhoto', 'MessageActionChatDeletePhoto'] = pydantic.Field(
        'types.MessageActionChatDeletePhoto',
        alias='_'
    )

