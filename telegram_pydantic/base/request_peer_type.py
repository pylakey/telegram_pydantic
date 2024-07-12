from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# RequestPeerType - Layer 181
RequestPeerType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.RequestPeerTypeBroadcast, pydantic.Tag('RequestPeerTypeBroadcast')],
        typing.Annotated[types.RequestPeerTypeChat, pydantic.Tag('RequestPeerTypeChat')],
        typing.Annotated[types.RequestPeerTypeUser, pydantic.Tag('RequestPeerTypeUser')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
