from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhoneContact(BaseModel):
    """
    types.InputPhoneContact
    ID: 0xf392b7f4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhoneContact', 'InputPhoneContact'] = pydantic.Field(
        'types.InputPhoneContact',
        alias='_'
    )

    client_id: int
    phone: str
    first_name: str
    last_name: str
