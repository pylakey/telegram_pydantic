from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.Messages - Layer 181
Messages = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.ChannelMessages, pydantic.Tag('messages.ChannelMessages')],
        typing.Annotated[types.messages.Messages, pydantic.Tag('messages.Messages')],
        typing.Annotated[types.messages.MessagesNotModified, pydantic.Tag('messages.MessagesNotModified')],
        typing.Annotated[types.messages.MessagesSlice, pydantic.Tag('messages.MessagesSlice')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
