from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChatInvite - Layer 181
ChatInvite = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChatInvite, pydantic.Tag('ChatInvite')],
        typing.Annotated[types.ChatInviteAlready, pydantic.Tag('ChatInviteAlready')],
        typing.Annotated[types.ChatInvitePeek, pydantic.Tag('ChatInvitePeek')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
