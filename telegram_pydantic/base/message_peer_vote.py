from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessagePeerVote - Layer 181
MessagePeerVote = typing.Annotated[
    typing.Union[
        typing.Annotated[types.MessagePeerVote, pydantic.Tag('MessagePeerVote')],
        typing.Annotated[types.MessagePeerVoteInputOption, pydantic.Tag('MessagePeerVoteInputOption')],
        typing.Annotated[types.MessagePeerVoteMultiple, pydantic.Tag('MessagePeerVoteMultiple')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
