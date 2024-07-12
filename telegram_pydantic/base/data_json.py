from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DataJSON - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
DataJSON = typing.Union[
    typing.Annotated[types.DataJSON, pydantic.Tag('DataJSON')]
]
