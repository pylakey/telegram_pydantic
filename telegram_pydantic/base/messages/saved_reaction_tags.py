from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.SavedReactionTags - Layer 181
SavedReactionTags = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.SavedReactionTags, pydantic.Tag('messages.SavedReactionTags')],
        typing.Annotated[types.messages.SavedReactionTagsNotModified, pydantic.Tag('messages.SavedReactionTagsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
