from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# chatlists.ChatlistUpdates - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
ChatlistUpdates = typing.Union[
    typing.Annotated[types.chatlists.ChatlistUpdates, pydantic.Tag('chatlists.ChatlistUpdates')]
]
