from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BotApp - Layer 181
BotApp = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BotApp, pydantic.Tag('BotApp')],
        typing.Annotated[types.BotAppNotModified, pydantic.Tag('BotAppNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
