from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputTheme - Layer 181
InputTheme = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputTheme, pydantic.Tag('InputTheme')],
        typing.Annotated[types.InputThemeSlug, pydantic.Tag('InputThemeSlug')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
