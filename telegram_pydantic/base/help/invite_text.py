from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.InviteText - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
InviteText = typing.Union[
    typing.Annotated[types.help.InviteText, pydantic.Tag('help.InviteText')]
]
