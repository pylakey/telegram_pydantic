from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.AvailableReactions - Layer 181
AvailableReactions = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.AvailableReactions, pydantic.Tag('messages.AvailableReactions')],
        typing.Annotated[types.messages.AvailableReactionsNotModified, pydantic.Tag('messages.AvailableReactionsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
