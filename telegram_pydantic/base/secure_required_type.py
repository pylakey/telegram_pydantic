from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SecureRequiredType - Layer 181
SecureRequiredType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SecureRequiredType, pydantic.Tag('SecureRequiredType')],
        typing.Annotated[types.SecureRequiredTypeOneOf, pydantic.Tag('SecureRequiredTypeOneOf')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
