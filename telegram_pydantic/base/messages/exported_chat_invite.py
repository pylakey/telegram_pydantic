from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.ExportedChatInvite - Layer 181
ExportedChatInvite = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.ExportedChatInvite, pydantic.Tag('messages.ExportedChatInvite')],
        typing.Annotated[types.messages.ExportedChatInviteReplaced, pydantic.Tag('messages.ExportedChatInviteReplaced')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
