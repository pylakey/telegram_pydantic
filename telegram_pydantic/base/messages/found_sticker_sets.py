from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.FoundStickerSets - Layer 181
FoundStickerSets = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.FoundStickerSets, pydantic.Tag('messages.FoundStickerSets')],
        typing.Annotated[types.messages.FoundStickerSetsNotModified, pydantic.Tag('messages.FoundStickerSetsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
