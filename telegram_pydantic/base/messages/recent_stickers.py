from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.RecentStickers - Layer 181
RecentStickers = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.RecentStickers, pydantic.Tag('messages.RecentStickers')],
        typing.Annotated[types.messages.RecentStickersNotModified, pydantic.Tag('messages.RecentStickersNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
