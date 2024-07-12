from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Updates - Layer 181
Updates = typing.Annotated[
    typing.Union[
        typing.Annotated[types.UpdateShort, pydantic.Tag('UpdateShort')],
        typing.Annotated[types.UpdateShortChatMessage, pydantic.Tag('UpdateShortChatMessage')],
        typing.Annotated[types.UpdateShortMessage, pydantic.Tag('UpdateShortMessage')],
        typing.Annotated[types.UpdateShortSentMessage, pydantic.Tag('UpdateShortSentMessage')],
        typing.Annotated[types.Updates, pydantic.Tag('Updates')],
        typing.Annotated[types.UpdatesCombined, pydantic.Tag('UpdatesCombined')],
        typing.Annotated[types.UpdatesTooLong, pydantic.Tag('UpdatesTooLong')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
