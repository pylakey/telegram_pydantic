from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EmailVerifyPurpose - Layer 181
EmailVerifyPurpose = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EmailVerifyPurposeLoginChange, pydantic.Tag('EmailVerifyPurposeLoginChange')],
        typing.Annotated[types.EmailVerifyPurposeLoginSetup, pydantic.Tag('EmailVerifyPurposeLoginSetup')],
        typing.Annotated[types.EmailVerifyPurposePassport, pydantic.Tag('EmailVerifyPurposePassport')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
