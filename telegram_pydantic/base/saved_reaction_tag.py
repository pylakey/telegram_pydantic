from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SavedReactionTag - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
SavedReactionTag = typing.Union[
    typing.Annotated[types.SavedReactionTag, pydantic.Tag('SavedReactionTag')]
]
