from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# DraftMessage - Layer 181
DraftMessage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.DraftMessage, pydantic.Tag('DraftMessage')],
        typing.Annotated[types.DraftMessageEmpty, pydantic.Tag('DraftMessageEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
