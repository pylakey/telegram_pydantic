from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputThemeSettings - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
InputThemeSettings = typing.Union[
    typing.Annotated[types.InputThemeSettings, pydantic.Tag('InputThemeSettings')]
]
