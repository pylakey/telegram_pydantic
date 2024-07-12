from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.EmojiGroups - Layer 181
EmojiGroups = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.EmojiGroups, pydantic.Tag('messages.EmojiGroups')],
        typing.Annotated[types.messages.EmojiGroupsNotModified, pydantic.Tag('messages.EmojiGroupsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
