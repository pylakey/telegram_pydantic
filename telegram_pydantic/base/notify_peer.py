from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# NotifyPeer - Layer 181
NotifyPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.NotifyBroadcasts, pydantic.Tag('NotifyBroadcasts')],
        typing.Annotated[types.NotifyChats, pydantic.Tag('NotifyChats')],
        typing.Annotated[types.NotifyForumTopic, pydantic.Tag('NotifyForumTopic')],
        typing.Annotated[types.NotifyPeer, pydantic.Tag('NotifyPeer')],
        typing.Annotated[types.NotifyUsers, pydantic.Tag('NotifyUsers')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
