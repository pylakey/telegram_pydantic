from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.SavedDialogs - Layer 181
SavedDialogs = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.SavedDialogs, pydantic.Tag('messages.SavedDialogs')],
        typing.Annotated[types.messages.SavedDialogsNotModified, pydantic.Tag('messages.SavedDialogsNotModified')],
        typing.Annotated[types.messages.SavedDialogsSlice, pydantic.Tag('messages.SavedDialogsSlice')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
