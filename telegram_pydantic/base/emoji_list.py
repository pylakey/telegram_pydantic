from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EmojiList - Layer 181
EmojiList = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EmojiList, pydantic.Tag('EmojiList')],
        typing.Annotated[types.EmojiListNotModified, pydantic.Tag('EmojiListNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
