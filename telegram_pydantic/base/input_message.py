from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputMessage - Layer 181
InputMessage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputMessageCallbackQuery, pydantic.Tag('InputMessageCallbackQuery')],
        typing.Annotated[types.InputMessageID, pydantic.Tag('InputMessageID')],
        typing.Annotated[types.InputMessagePinned, pydantic.Tag('InputMessagePinned')],
        typing.Annotated[types.InputMessageReplyTo, pydantic.Tag('InputMessageReplyTo')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
