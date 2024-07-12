from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.ForumTopics - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
ForumTopics = typing.Union[
    typing.Annotated[types.messages.ForumTopics, pydantic.Tag('messages.ForumTopics')]
]
