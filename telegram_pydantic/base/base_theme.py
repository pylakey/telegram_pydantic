from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BaseTheme - Layer 181
BaseTheme = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BaseThemeArctic, pydantic.Tag('BaseThemeArctic')],
        typing.Annotated[types.BaseThemeClassic, pydantic.Tag('BaseThemeClassic')],
        typing.Annotated[types.BaseThemeDay, pydantic.Tag('BaseThemeDay')],
        typing.Annotated[types.BaseThemeNight, pydantic.Tag('BaseThemeNight')],
        typing.Annotated[types.BaseThemeTinted, pydantic.Tag('BaseThemeTinted')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
