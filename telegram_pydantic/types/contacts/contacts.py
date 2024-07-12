from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Contacts(BaseModel):
    """
    types.contacts.Contacts
    ID: 0xeae87e42
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.Contacts', 'Contacts'] = pydantic.Field(
        'types.contacts.Contacts',
        alias='_'
    )

    contacts: list["base.Contact"]
    saved_count: int
    users: list["base.User"]
