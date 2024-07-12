from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportContacts(BaseModel):
    """
    functions.contacts.ImportContacts
    ID: 0x2c800be5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ImportContacts', 'ImportContacts'] = pydantic.Field(
        'functions.contacts.ImportContacts',
        alias='_'
    )

    contacts: list["base.InputContact"]
