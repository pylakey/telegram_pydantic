from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChannelParticipant - Layer 181
ChannelParticipant = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChannelParticipant, pydantic.Tag('ChannelParticipant')],
        typing.Annotated[types.ChannelParticipantAdmin, pydantic.Tag('ChannelParticipantAdmin')],
        typing.Annotated[types.ChannelParticipantBanned, pydantic.Tag('ChannelParticipantBanned')],
        typing.Annotated[types.ChannelParticipantCreator, pydantic.Tag('ChannelParticipantCreator')],
        typing.Annotated[types.ChannelParticipantLeft, pydantic.Tag('ChannelParticipantLeft')],
        typing.Annotated[types.ChannelParticipantSelf, pydantic.Tag('ChannelParticipantSelf')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
