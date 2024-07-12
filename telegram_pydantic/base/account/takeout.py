from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.Takeout - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
Takeout = typing.Union[
    typing.Annotated[types.account.Takeout, pydantic.Tag('account.Takeout')]
]
