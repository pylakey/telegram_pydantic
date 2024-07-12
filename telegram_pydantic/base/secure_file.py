from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SecureFile - Layer 181
SecureFile = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SecureFile, pydantic.Tag('SecureFile')],
        typing.Annotated[types.SecureFileEmpty, pydantic.Tag('SecureFileEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
