from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# StoryItem - Layer 181
StoryItem = typing.Annotated[
    typing.Union[
        typing.Annotated[types.StoryItem, pydantic.Tag('StoryItem')],
        typing.Annotated[types.StoryItemDeleted, pydantic.Tag('StoryItemDeleted')],
        typing.Annotated[types.StoryItemSkipped, pydantic.Tag('StoryItemSkipped')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
