from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.ResolvedPeer - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
ResolvedPeer = typing.Union[
    typing.Annotated[types.contacts.ResolvedPeer, pydantic.Tag('contacts.ResolvedPeer')]
]
