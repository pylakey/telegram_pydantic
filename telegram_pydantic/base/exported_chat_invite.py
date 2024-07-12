from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ExportedChatInvite - Layer 181
ExportedChatInvite = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChatInviteExported, pydantic.Tag('ChatInviteExported')],
        typing.Annotated[types.ChatInvitePublicJoinRequests, pydantic.Tag('ChatInvitePublicJoinRequests')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
