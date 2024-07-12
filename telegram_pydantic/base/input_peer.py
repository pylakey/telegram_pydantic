from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputPeer - Layer 181
InputPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputPeerChannel, pydantic.Tag('InputPeerChannel')],
        typing.Annotated[types.InputPeerChannelFromMessage, pydantic.Tag('InputPeerChannelFromMessage')],
        typing.Annotated[types.InputPeerChat, pydantic.Tag('InputPeerChat')],
        typing.Annotated[types.InputPeerEmpty, pydantic.Tag('InputPeerEmpty')],
        typing.Annotated[types.InputPeerSelf, pydantic.Tag('InputPeerSelf')],
        typing.Annotated[types.InputPeerUser, pydantic.Tag('InputPeerUser')],
        typing.Annotated[types.InputPeerUserFromMessage, pydantic.Tag('InputPeerUserFromMessage')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
