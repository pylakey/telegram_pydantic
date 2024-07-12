from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# contacts.Blocked - Layer 181
Blocked = typing.Annotated[
    typing.Union[
        typing.Annotated[types.contacts.Blocked, pydantic.Tag('contacts.Blocked')],
        typing.Annotated[types.contacts.BlockedSlice, pydantic.Tag('contacts.BlockedSlice')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
