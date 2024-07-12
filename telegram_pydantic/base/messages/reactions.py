from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.Reactions - Layer 181
Reactions = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.Reactions, pydantic.Tag('messages.Reactions')],
        typing.Annotated[types.messages.ReactionsNotModified, pydantic.Tag('messages.ReactionsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
