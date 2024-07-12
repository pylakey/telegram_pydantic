from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# stories.AllStories - Layer 181
AllStories = typing.Annotated[
    typing.Union[
        typing.Annotated[types.stories.AllStories, pydantic.Tag('stories.AllStories')],
        typing.Annotated[types.stories.AllStoriesNotModified, pydantic.Tag('stories.AllStoriesNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
