from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# LangPackLanguage - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
LangPackLanguage = typing.Union[
    typing.Annotated[types.LangPackLanguage, pydantic.Tag('LangPackLanguage')]
]
