from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.AvailableEffects - Layer 181
AvailableEffects = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.AvailableEffects, pydantic.Tag('messages.AvailableEffects')],
        typing.Annotated[types.messages.AvailableEffectsNotModified, pydantic.Tag('messages.AvailableEffectsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
