from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# RecentMeUrl - Layer 181
RecentMeUrl = typing.Annotated[
    typing.Union[
        typing.Annotated[types.RecentMeUrlChat, pydantic.Tag('RecentMeUrlChat')],
        typing.Annotated[types.RecentMeUrlChatInvite, pydantic.Tag('RecentMeUrlChatInvite')],
        typing.Annotated[types.RecentMeUrlStickerSet, pydantic.Tag('RecentMeUrlStickerSet')],
        typing.Annotated[types.RecentMeUrlUnknown, pydantic.Tag('RecentMeUrlUnknown')],
        typing.Annotated[types.RecentMeUrlUser, pydantic.Tag('RecentMeUrlUser')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
