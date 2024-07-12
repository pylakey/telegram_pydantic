from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PasswordKdfAlgo - Layer 181
PasswordKdfAlgo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow, pydantic.Tag('PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow')],
        typing.Annotated[types.PasswordKdfAlgoUnknown, pydantic.Tag('PasswordKdfAlgoUnknown')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
