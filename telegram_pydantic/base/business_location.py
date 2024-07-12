from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessLocation - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
BusinessLocation = typing.Union[
    typing.Annotated[types.BusinessLocation, pydantic.Tag('BusinessLocation')]
]
