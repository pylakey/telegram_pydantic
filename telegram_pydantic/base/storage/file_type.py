from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# storage.FileType - Layer 181
FileType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.storage.FileGif, pydantic.Tag('storage.FileGif')],
        typing.Annotated[types.storage.FileJpeg, pydantic.Tag('storage.FileJpeg')],
        typing.Annotated[types.storage.FileMov, pydantic.Tag('storage.FileMov')],
        typing.Annotated[types.storage.FileMp3, pydantic.Tag('storage.FileMp3')],
        typing.Annotated[types.storage.FileMp4, pydantic.Tag('storage.FileMp4')],
        typing.Annotated[types.storage.FilePartial, pydantic.Tag('storage.FilePartial')],
        typing.Annotated[types.storage.FilePdf, pydantic.Tag('storage.FilePdf')],
        typing.Annotated[types.storage.FilePng, pydantic.Tag('storage.FilePng')],
        typing.Annotated[types.storage.FileUnknown, pydantic.Tag('storage.FileUnknown')],
        typing.Annotated[types.storage.FileWebp, pydantic.Tag('storage.FileWebp')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
