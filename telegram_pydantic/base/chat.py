from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Chat - Layer 181
Chat = typing.Annotated[
    typing.Union[
        typing.Annotated[types.Channel, pydantic.Tag('Channel')],
        typing.Annotated[types.ChannelForbidden, pydantic.Tag('ChannelForbidden')],
        typing.Annotated[types.Chat, pydantic.Tag('Chat')],
        typing.Annotated[types.ChatEmpty, pydantic.Tag('ChatEmpty')],
        typing.Annotated[types.ChatForbidden, pydantic.Tag('ChatForbidden')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
