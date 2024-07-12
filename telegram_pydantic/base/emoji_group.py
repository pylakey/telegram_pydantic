from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EmojiGroup - Layer 181
EmojiGroup = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EmojiGroup, pydantic.Tag('EmojiGroup')],
        typing.Annotated[types.EmojiGroupGreeting, pydantic.Tag('EmojiGroupGreeting')],
        typing.Annotated[types.EmojiGroupPremium, pydantic.Tag('EmojiGroupPremium')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
