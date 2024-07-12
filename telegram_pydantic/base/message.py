from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Message - Layer 181
Message = typing.Annotated[
    typing.Union[
        typing.Annotated[types.Message, pydantic.Tag('Message')],
        typing.Annotated[types.MessageEmpty, pydantic.Tag('MessageEmpty')],
        typing.Annotated[types.MessageService, pydantic.Tag('MessageService')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
