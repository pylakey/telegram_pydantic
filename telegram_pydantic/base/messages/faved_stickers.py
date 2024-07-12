from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.FavedStickers - Layer 181
FavedStickers = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.FavedStickers, pydantic.Tag('messages.FavedStickers')],
        typing.Annotated[types.messages.FavedStickersNotModified, pydantic.Tag('messages.FavedStickersNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
