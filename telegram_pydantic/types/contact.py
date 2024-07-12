from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Contact(BaseModel):
    """
    types.Contact
    ID: 0x145ade0b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Contact', 'Contact'] = pydantic.Field(
        'types.Contact',
        alias='_'
    )

    user_id: int
    mutual: bool
