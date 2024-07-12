from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetContacts(BaseModel):
    """
    functions.contacts.GetContacts
    ID: 0x5dd69e12
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetContacts', 'GetContacts'] = pydantic.Field(
        'functions.contacts.GetContacts',
        alias='_'
    )

    hash: int
