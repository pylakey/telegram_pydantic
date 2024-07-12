from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChatParticipants - Layer 181
ChatParticipants = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChatParticipants, pydantic.Tag('ChatParticipants')],
        typing.Annotated[types.ChatParticipantsForbidden, pydantic.Tag('ChatParticipantsForbidden')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
