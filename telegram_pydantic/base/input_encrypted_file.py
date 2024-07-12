from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputEncryptedFile - Layer 181
InputEncryptedFile = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputEncryptedFile, pydantic.Tag('InputEncryptedFile')],
        typing.Annotated[types.InputEncryptedFileBigUploaded, pydantic.Tag('InputEncryptedFileBigUploaded')],
        typing.Annotated[types.InputEncryptedFileEmpty, pydantic.Tag('InputEncryptedFileEmpty')],
        typing.Annotated[types.InputEncryptedFileUploaded, pydantic.Tag('InputEncryptedFileUploaded')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
