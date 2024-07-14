from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# channels.ChannelParticipants - Layer 181
ChannelParticipants = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.channels.ChannelParticipants,
            pydantic.Tag('channels.ChannelParticipants'),
            pydantic.Tag('ChannelParticipants')
        ],
        typing.Annotated[
            types.channels.ChannelParticipantsNotModified,
            pydantic.Tag('channels.ChannelParticipantsNotModified'),
            pydantic.Tag('ChannelParticipantsNotModified')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
