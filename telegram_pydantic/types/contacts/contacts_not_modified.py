from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContactsNotModified(BaseModel):
    """
    types.contacts.ContactsNotModified
    ID: 0xb74ba9d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.ContactsNotModified', 'ContactsNotModified'] = pydantic.Field(
        'types.contacts.ContactsNotModified',
        alias='_'
    )

