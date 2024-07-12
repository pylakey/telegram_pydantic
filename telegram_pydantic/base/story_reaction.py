from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# StoryReaction - Layer 181
StoryReaction = typing.Annotated[
    typing.Union[
        typing.Annotated[types.StoryReaction, pydantic.Tag('StoryReaction')],
        typing.Annotated[types.StoryReactionPublicForward, pydantic.Tag('StoryReactionPublicForward')],
        typing.Annotated[types.StoryReactionPublicRepost, pydantic.Tag('StoryReactionPublicRepost')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
