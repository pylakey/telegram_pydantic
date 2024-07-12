from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# contacts.Contacts - Layer 181
Contacts = typing.Annotated[
    typing.Union[
        typing.Annotated[types.contacts.Contacts, pydantic.Tag('contacts.Contacts')],
        typing.Annotated[types.contacts.ContactsNotModified, pydantic.Tag('contacts.ContactsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
