from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.SponsoredMessages - Layer 181
SponsoredMessages = typing.Annotated[
    typing.Union[
        typing.Annotated[types.messages.SponsoredMessages, pydantic.Tag('messages.SponsoredMessages')],
        typing.Annotated[types.messages.SponsoredMessagesEmpty, pydantic.Tag('messages.SponsoredMessagesEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
