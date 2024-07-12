from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputNotifyPeer - Layer 181
InputNotifyPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputNotifyBroadcasts, pydantic.Tag('InputNotifyBroadcasts')],
        typing.Annotated[types.InputNotifyChats, pydantic.Tag('InputNotifyChats')],
        typing.Annotated[types.InputNotifyForumTopic, pydantic.Tag('InputNotifyForumTopic')],
        typing.Annotated[types.InputNotifyPeer, pydantic.Tag('InputNotifyPeer')],
        typing.Annotated[types.InputNotifyUsers, pydantic.Tag('InputNotifyUsers')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
