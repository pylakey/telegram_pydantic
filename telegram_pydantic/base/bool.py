from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Bool - Layer 181
Bool = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BoolFalse, pydantic.Tag('BoolFalse')],
        typing.Annotated[types.BoolTrue, pydantic.Tag('BoolTrue')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
