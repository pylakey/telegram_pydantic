from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.Stories - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
Stories = typing.Union[
    typing.Annotated[types.stories.Stories, pydantic.Tag('stories.Stories')]
]
