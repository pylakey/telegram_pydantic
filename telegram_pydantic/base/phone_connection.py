from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PhoneConnection - Layer 181
PhoneConnection = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PhoneConnection, pydantic.Tag('PhoneConnection')],
        typing.Annotated[types.PhoneConnectionWebrtc, pydantic.Tag('PhoneConnectionWebrtc')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
