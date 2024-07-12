from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EncryptedFile - Layer 181
EncryptedFile = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EncryptedFile, pydantic.Tag('EncryptedFile')],
        typing.Annotated[types.EncryptedFileEmpty, pydantic.Tag('EncryptedFileEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
