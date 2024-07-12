from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.ResetPasswordResult - Layer 181
ResetPasswordResult = typing.Annotated[
    typing.Union[
        typing.Annotated[types.account.ResetPasswordFailedWait, pydantic.Tag('account.ResetPasswordFailedWait')],
        typing.Annotated[types.account.ResetPasswordOk, pydantic.Tag('account.ResetPasswordOk')],
        typing.Annotated[types.account.ResetPasswordRequestedWait, pydantic.Tag('account.ResetPasswordRequestedWait')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
