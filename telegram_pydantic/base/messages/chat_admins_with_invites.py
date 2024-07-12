from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ChatAdminsWithInvites - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
ChatAdminsWithInvites = typing.Union[
    typing.Annotated[types.messages.ChatAdminsWithInvites, pydantic.Tag('messages.ChatAdminsWithInvites')]
]
