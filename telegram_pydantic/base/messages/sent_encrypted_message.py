from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.SentEncryptedMessage - Layer 181
SentEncryptedMessage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.SentEncryptedFile, pydantic.Tag('messages.SentEncryptedFile')],
        typing.Annotated[types.messages.SentEncryptedMessage, pydantic.Tag('messages.SentEncryptedMessage')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
