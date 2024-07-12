from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Reaction - Layer 181
Reaction = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ReactionCustomEmoji, pydantic.Tag('ReactionCustomEmoji')],
        typing.Annotated[types.ReactionEmoji, pydantic.Tag('ReactionEmoji')],
        typing.Annotated[types.ReactionEmpty, pydantic.Tag('ReactionEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
