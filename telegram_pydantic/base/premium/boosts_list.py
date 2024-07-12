from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# premium.BoostsList - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
BoostsList = typing.Union[
    typing.Annotated[types.premium.BoostsList, pydantic.Tag('premium.BoostsList')]
]
