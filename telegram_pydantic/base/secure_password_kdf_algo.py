from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SecurePasswordKdfAlgo - Layer 181
SecurePasswordKdfAlgo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000, pydantic.Tag('SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000')],
        typing.Annotated[types.SecurePasswordKdfAlgoSHA512, pydantic.Tag('SecurePasswordKdfAlgoSHA512')],
        typing.Annotated[types.SecurePasswordKdfAlgoUnknown, pydantic.Tag('SecurePasswordKdfAlgoUnknown')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
