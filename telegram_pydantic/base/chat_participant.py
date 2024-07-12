from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChatParticipant - Layer 181
ChatParticipant = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChatParticipant, pydantic.Tag('ChatParticipant')],
        typing.Annotated[types.ChatParticipantAdmin, pydantic.Tag('ChatParticipantAdmin')],
        typing.Annotated[types.ChatParticipantCreator, pydantic.Tag('ChatParticipantCreator')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
