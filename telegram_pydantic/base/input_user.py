from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputUser - Layer 181
InputUser = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputUser, pydantic.Tag('InputUser')],
        typing.Annotated[types.InputUserEmpty, pydantic.Tag('InputUserEmpty')],
        typing.Annotated[types.InputUserFromMessage, pydantic.Tag('InputUserFromMessage')],
        typing.Annotated[types.InputUserSelf, pydantic.Tag('InputUserSelf')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
