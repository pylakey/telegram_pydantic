from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatEditPhoto(BaseModel):
    """
    types.MessageActionChatEditPhoto
    ID: 0x7fcb13a8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatEditPhoto', 'MessageActionChatEditPhoto'] = pydantic.Field(
        'types.MessageActionChatEditPhoto',
        alias='_'
    )

    photo: "base.Photo"
