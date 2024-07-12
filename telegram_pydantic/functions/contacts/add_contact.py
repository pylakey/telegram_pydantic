from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AddContact(BaseModel):
    """
    functions.contacts.AddContact
    ID: 0xe8f463d0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.AddContact', 'AddContact'] = pydantic.Field(
        'functions.contacts.AddContact',
        alias='_'
    )

    id: "base.InputUser"
    first_name: str
    last_name: str
    phone: str
    add_phone_privacy_exception: typing.Optional[bool] = None
