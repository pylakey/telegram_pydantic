from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# auth.SentCode - Layer 181
SentCode = typing.Annotated[
    typing.Union[
        typing.Annotated[types.auth.SentCode, pydantic.Tag('auth.SentCode')],
        typing.Annotated[types.auth.SentCodeSuccess, pydantic.Tag('auth.SentCodeSuccess')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
