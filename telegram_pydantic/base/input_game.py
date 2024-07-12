from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputGame - Layer 181
InputGame = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputGameID, pydantic.Tag('InputGameID')],
        typing.Annotated[types.InputGameShortName, pydantic.Tag('InputGameShortName')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
