from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# upload.File - Layer 181
File = typing.Annotated[
    typing.Union[
        typing.Annotated[types.upload.File, pydantic.Tag('upload.File')],
        typing.Annotated[types.upload.FileCdnRedirect, pydantic.Tag('upload.FileCdnRedirect')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
