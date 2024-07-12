from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EncryptedChat - Layer 181
EncryptedChat = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EncryptedChat, pydantic.Tag('EncryptedChat')],
        typing.Annotated[types.EncryptedChatDiscarded, pydantic.Tag('EncryptedChatDiscarded')],
        typing.Annotated[types.EncryptedChatEmpty, pydantic.Tag('EncryptedChatEmpty')],
        typing.Annotated[types.EncryptedChatRequested, pydantic.Tag('EncryptedChatRequested')],
        typing.Annotated[types.EncryptedChatWaiting, pydantic.Tag('EncryptedChatWaiting')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
