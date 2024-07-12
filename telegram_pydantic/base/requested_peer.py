from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# RequestedPeer - Layer 181
RequestedPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.RequestedPeerChannel, pydantic.Tag('RequestedPeerChannel')],
        typing.Annotated[types.RequestedPeerChat, pydantic.Tag('RequestedPeerChat')],
        typing.Annotated[types.RequestedPeerUser, pydantic.Tag('RequestedPeerUser')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
