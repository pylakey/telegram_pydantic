from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# upload.CdnFile - Layer 181
CdnFile = typing.Annotated[
    typing.Union[
        typing.Annotated[types.upload.CdnFile, pydantic.Tag('upload.CdnFile')],
        typing.Annotated[types.upload.CdnFileReuploadNeeded, pydantic.Tag('upload.CdnFileReuploadNeeded')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
