from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputCheckPasswordSRP - Layer 181
InputCheckPasswordSRP = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputCheckPasswordEmpty, pydantic.Tag('InputCheckPasswordEmpty')],
        typing.Annotated[types.InputCheckPasswordSRP, pydantic.Tag('InputCheckPasswordSRP')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
