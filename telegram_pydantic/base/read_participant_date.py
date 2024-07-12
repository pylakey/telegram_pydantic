from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReadParticipantDate - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
ReadParticipantDate = typing.Union[
    typing.Annotated[types.ReadParticipantDate, pydantic.Tag('ReadParticipantDate')]
]
