from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EncryptedMessage - Layer 181
EncryptedMessage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EncryptedMessage, pydantic.Tag('EncryptedMessage')],
        typing.Annotated[types.EncryptedMessageService, pydantic.Tag('EncryptedMessageService')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
