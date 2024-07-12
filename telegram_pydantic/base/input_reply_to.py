from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputReplyTo - Layer 181
InputReplyTo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputReplyToMessage, pydantic.Tag('InputReplyToMessage')],
        typing.Annotated[types.InputReplyToStory, pydantic.Tag('InputReplyToStory')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
