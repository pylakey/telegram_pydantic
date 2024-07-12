from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.FeaturedStickers - Layer 181
FeaturedStickers = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.FeaturedStickers, pydantic.Tag('messages.FeaturedStickers')],
        typing.Annotated[types.messages.FeaturedStickersNotModified, pydantic.Tag('messages.FeaturedStickersNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
