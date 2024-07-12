from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.DhConfig - Layer 181
DhConfig = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.DhConfig, pydantic.Tag('messages.DhConfig')],
        typing.Annotated[types.messages.DhConfigNotModified, pydantic.Tag('messages.DhConfigNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
