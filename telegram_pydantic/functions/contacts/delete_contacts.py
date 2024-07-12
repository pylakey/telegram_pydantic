from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteContacts(BaseModel):
    """
    functions.contacts.DeleteContacts
    ID: 0x96a0e00
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.DeleteContacts', 'DeleteContacts'] = pydantic.Field(
        'functions.contacts.DeleteContacts',
        alias='_'
    )

    id: list["base.InputUser"]
