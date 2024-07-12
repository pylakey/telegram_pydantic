from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# auth.Authorization - Layer 181
Authorization = typing.Annotated[
    typing.Union[
        typing.Annotated[types.auth.Authorization, pydantic.Tag('auth.Authorization')],
        typing.Annotated[types.auth.AuthorizationSignUpRequired, pydantic.Tag('auth.AuthorizationSignUpRequired')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
