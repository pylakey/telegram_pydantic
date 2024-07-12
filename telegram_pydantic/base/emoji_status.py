from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EmojiStatus - Layer 181
EmojiStatus = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EmojiStatus, pydantic.Tag('EmojiStatus')],
        typing.Annotated[types.EmojiStatusEmpty, pydantic.Tag('EmojiStatusEmpty')],
        typing.Annotated[types.EmojiStatusUntil, pydantic.Tag('EmojiStatusUntil')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
