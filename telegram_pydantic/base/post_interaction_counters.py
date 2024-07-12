from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PostInteractionCounters - Layer 181
PostInteractionCounters = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PostInteractionCountersMessage, pydantic.Tag('PostInteractionCountersMessage')],
        typing.Annotated[types.PostInteractionCountersStory, pydantic.Tag('PostInteractionCountersStory')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
