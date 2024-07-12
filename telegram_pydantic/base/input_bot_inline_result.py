from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputBotInlineResult - Layer 181
InputBotInlineResult = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputBotInlineResult, pydantic.Tag('InputBotInlineResult')],
        typing.Annotated[types.InputBotInlineResultDocument, pydantic.Tag('InputBotInlineResultDocument')],
        typing.Annotated[types.InputBotInlineResultGame, pydantic.Tag('InputBotInlineResultGame')],
        typing.Annotated[types.InputBotInlineResultPhoto, pydantic.Tag('InputBotInlineResultPhoto')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
