from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BotInlineResult - Layer 181
BotInlineResult = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BotInlineMediaResult, pydantic.Tag('BotInlineMediaResult')],
        typing.Annotated[types.BotInlineResult, pydantic.Tag('BotInlineResult')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
