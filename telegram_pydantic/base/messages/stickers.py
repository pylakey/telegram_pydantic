from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.Stickers - Layer 181
Stickers = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.Stickers, pydantic.Tag('messages.Stickers')],
        typing.Annotated[types.messages.StickersNotModified, pydantic.Tag('messages.StickersNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
