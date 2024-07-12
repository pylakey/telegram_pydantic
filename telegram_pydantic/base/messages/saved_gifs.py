from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.SavedGifs - Layer 181
SavedGifs = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.SavedGifs, pydantic.Tag('messages.SavedGifs')],
        typing.Annotated[types.messages.SavedGifsNotModified, pydantic.Tag('messages.SavedGifsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
