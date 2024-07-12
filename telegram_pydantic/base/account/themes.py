from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.Themes - Layer 181
Themes = typing.Annotated[
    typing.Union[
        typing.Annotated[types.account.Themes, pydantic.Tag('account.Themes')],
        typing.Annotated[types.account.ThemesNotModified, pydantic.Tag('account.ThemesNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
