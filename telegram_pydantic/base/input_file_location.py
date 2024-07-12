from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputFileLocation - Layer 181
InputFileLocation = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputDocumentFileLocation, pydantic.Tag('InputDocumentFileLocation')],
        typing.Annotated[types.InputEncryptedFileLocation, pydantic.Tag('InputEncryptedFileLocation')],
        typing.Annotated[types.InputFileLocation, pydantic.Tag('InputFileLocation')],
        typing.Annotated[types.InputGroupCallStream, pydantic.Tag('InputGroupCallStream')],
        typing.Annotated[types.InputPeerPhotoFileLocation, pydantic.Tag('InputPeerPhotoFileLocation')],
        typing.Annotated[types.InputPhotoFileLocation, pydantic.Tag('InputPhotoFileLocation')],
        typing.Annotated[types.InputPhotoLegacyFileLocation, pydantic.Tag('InputPhotoLegacyFileLocation')],
        typing.Annotated[types.InputSecureFileLocation, pydantic.Tag('InputSecureFileLocation')],
        typing.Annotated[types.InputStickerSetThumb, pydantic.Tag('InputStickerSetThumb')],
        typing.Annotated[types.InputTakeoutFileLocation, pydantic.Tag('InputTakeoutFileLocation')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
