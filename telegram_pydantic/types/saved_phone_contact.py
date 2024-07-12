from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedPhoneContact(BaseModel):
    """
    types.SavedPhoneContact
    ID: 0x1142bd56
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SavedPhoneContact', 'SavedPhoneContact'] = pydantic.Field(
        'types.SavedPhoneContact',
        alias='_'
    )

    phone: str
    first_name: str
    last_name: str
    date: Datetime
