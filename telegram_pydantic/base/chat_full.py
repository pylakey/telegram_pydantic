from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChatFull - Layer 181
ChatFull = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChannelFull, pydantic.Tag('ChannelFull')],
        typing.Annotated[types.ChatFull, pydantic.Tag('ChatFull')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
