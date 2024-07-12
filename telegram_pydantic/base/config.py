from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Config - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
Config = typing.Union[
    typing.Annotated[types.Config, pydantic.Tag('Config')]
]
