from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BotMenuButton - Layer 181
BotMenuButton = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BotMenuButton, pydantic.Tag('BotMenuButton')],
        typing.Annotated[types.BotMenuButtonCommands, pydantic.Tag('BotMenuButtonCommands')],
        typing.Annotated[types.BotMenuButtonDefault, pydantic.Tag('BotMenuButtonDefault')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
