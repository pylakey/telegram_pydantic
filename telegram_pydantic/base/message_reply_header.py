from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessageReplyHeader - Layer 181
MessageReplyHeader = typing.Annotated[
    typing.Union[
        typing.Annotated[types.MessageReplyHeader, pydantic.Tag('MessageReplyHeader')],
        typing.Annotated[types.MessageReplyStoryHeader, pydantic.Tag('MessageReplyStoryHeader')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
