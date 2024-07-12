from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# User - Layer 181
User = typing.Annotated[
    typing.Union[
        typing.Annotated[types.User, pydantic.Tag('User')],
        typing.Annotated[types.UserEmpty, pydantic.Tag('UserEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
