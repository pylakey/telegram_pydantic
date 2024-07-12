from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChannelParticipantsFilter - Layer 181
ChannelParticipantsFilter = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChannelParticipantsAdmins, pydantic.Tag('ChannelParticipantsAdmins')],
        typing.Annotated[types.ChannelParticipantsBanned, pydantic.Tag('ChannelParticipantsBanned')],
        typing.Annotated[types.ChannelParticipantsBots, pydantic.Tag('ChannelParticipantsBots')],
        typing.Annotated[types.ChannelParticipantsContacts, pydantic.Tag('ChannelParticipantsContacts')],
        typing.Annotated[types.ChannelParticipantsKicked, pydantic.Tag('ChannelParticipantsKicked')],
        typing.Annotated[types.ChannelParticipantsMentions, pydantic.Tag('ChannelParticipantsMentions')],
        typing.Annotated[types.ChannelParticipantsRecent, pydantic.Tag('ChannelParticipantsRecent')],
        typing.Annotated[types.ChannelParticipantsSearch, pydantic.Tag('ChannelParticipantsSearch')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
