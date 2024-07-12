from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.QuickReplies - Layer 181
QuickReplies = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.QuickReplies, pydantic.Tag('messages.QuickReplies')],
        typing.Annotated[types.messages.QuickRepliesNotModified, pydantic.Tag('messages.QuickRepliesNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
