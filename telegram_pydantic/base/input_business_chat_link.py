from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputBusinessChatLink - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
InputBusinessChatLink = typing.Union[
    typing.Annotated[types.InputBusinessChatLink, pydantic.Tag('InputBusinessChatLink')]
]
