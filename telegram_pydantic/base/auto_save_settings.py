from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AutoSaveSettings - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
AutoSaveSettings = typing.Union[
    typing.Annotated[types.AutoSaveSettings, pydantic.Tag('AutoSaveSettings')]
]
