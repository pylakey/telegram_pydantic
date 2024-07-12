from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaContact(BaseModel):
    """
    types.MessageMediaContact
    ID: 0x70322949
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaContact', 'MessageMediaContact'] = pydantic.Field(
        'types.MessageMediaContact',
        alias='_'
    )

    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    user_id: int
