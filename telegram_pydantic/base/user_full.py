from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# UserFull - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
UserFull = typing.Union[
    typing.Annotated[types.UserFull, pydantic.Tag('UserFull')]
]
