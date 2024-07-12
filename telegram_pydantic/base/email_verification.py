from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EmailVerification - Layer 181
EmailVerification = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EmailVerificationApple, pydantic.Tag('EmailVerificationApple')],
        typing.Annotated[types.EmailVerificationCode, pydantic.Tag('EmailVerificationCode')],
        typing.Annotated[types.EmailVerificationGoogle, pydantic.Tag('EmailVerificationGoogle')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
