from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputBotInlineMessageID - Layer 181
InputBotInlineMessageID = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputBotInlineMessageID, pydantic.Tag('InputBotInlineMessageID')],
        typing.Annotated[types.InputBotInlineMessageID64, pydantic.Tag('InputBotInlineMessageID64')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
