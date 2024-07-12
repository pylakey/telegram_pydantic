from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.Chats - Layer 181
Chats = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.Chats, pydantic.Tag('messages.Chats')],
        typing.Annotated[types.messages.ChatsSlice, pydantic.Tag('messages.ChatsSlice')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
