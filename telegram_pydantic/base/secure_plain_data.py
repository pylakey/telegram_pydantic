from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SecurePlainData - Layer 181
SecurePlainData = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SecurePlainEmail, pydantic.Tag('SecurePlainEmail')],
        typing.Annotated[types.SecurePlainPhone, pydantic.Tag('SecurePlainPhone')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
