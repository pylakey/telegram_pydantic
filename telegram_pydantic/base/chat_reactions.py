from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChatReactions - Layer 181
ChatReactions = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChatReactionsAll, pydantic.Tag('ChatReactionsAll')],
        typing.Annotated[types.ChatReactionsNone, pydantic.Tag('ChatReactionsNone')],
        typing.Annotated[types.ChatReactionsSome, pydantic.Tag('ChatReactionsSome')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
