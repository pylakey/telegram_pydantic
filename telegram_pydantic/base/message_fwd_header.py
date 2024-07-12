from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageFwdHeader - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
MessageFwdHeader = typing.Union[
    typing.Annotated[types.MessageFwdHeader, pydantic.Tag('MessageFwdHeader')]
]
