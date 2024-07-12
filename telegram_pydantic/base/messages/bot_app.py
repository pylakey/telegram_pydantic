from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.BotApp - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
BotApp = typing.Union[
    typing.Annotated[types.messages.BotApp, pydantic.Tag('messages.BotApp')]
]
