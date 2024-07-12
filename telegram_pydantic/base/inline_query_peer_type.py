from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InlineQueryPeerType - Layer 181
InlineQueryPeerType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InlineQueryPeerTypeBotPM, pydantic.Tag('InlineQueryPeerTypeBotPM')],
        typing.Annotated[types.InlineQueryPeerTypeBroadcast, pydantic.Tag('InlineQueryPeerTypeBroadcast')],
        typing.Annotated[types.InlineQueryPeerTypeChat, pydantic.Tag('InlineQueryPeerTypeChat')],
        typing.Annotated[types.InlineQueryPeerTypeMegagroup, pydantic.Tag('InlineQueryPeerTypeMegagroup')],
        typing.Annotated[types.InlineQueryPeerTypePM, pydantic.Tag('InlineQueryPeerTypePM')],
        typing.Annotated[types.InlineQueryPeerTypeSameBotPM, pydantic.Tag('InlineQueryPeerTypeSameBotPM')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
