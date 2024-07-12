from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# StoryView - Layer 181
StoryView = typing.Annotated[
    typing.Union[
        typing.Annotated[types.StoryView, pydantic.Tag('StoryView')],
        typing.Annotated[types.StoryViewPublicForward, pydantic.Tag('StoryViewPublicForward')],
        typing.Annotated[types.StoryViewPublicRepost, pydantic.Tag('StoryViewPublicRepost')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
