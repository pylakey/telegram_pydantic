from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# AttachMenuPeerType - Layer 181
AttachMenuPeerType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.AttachMenuPeerTypeBotPM, pydantic.Tag('AttachMenuPeerTypeBotPM')],
        typing.Annotated[types.AttachMenuPeerTypeBroadcast, pydantic.Tag('AttachMenuPeerTypeBroadcast')],
        typing.Annotated[types.AttachMenuPeerTypeChat, pydantic.Tag('AttachMenuPeerTypeChat')],
        typing.Annotated[types.AttachMenuPeerTypePM, pydantic.Tag('AttachMenuPeerTypePM')],
        typing.Annotated[types.AttachMenuPeerTypeSameBotPM, pydantic.Tag('AttachMenuPeerTypeSameBotPM')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
