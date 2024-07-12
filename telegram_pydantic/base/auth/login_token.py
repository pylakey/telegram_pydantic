from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# auth.LoginToken - Layer 181
LoginToken = typing.Annotated[
    typing.Union[
        typing.Annotated[types.auth.LoginToken, pydantic.Tag('auth.LoginToken')],
        typing.Annotated[types.auth.LoginTokenMigrateTo, pydantic.Tag('auth.LoginTokenMigrateTo')],
        typing.Annotated[types.auth.LoginTokenSuccess, pydantic.Tag('auth.LoginTokenSuccess')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
