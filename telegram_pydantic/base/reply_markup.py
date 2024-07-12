from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ReplyMarkup - Layer 181
ReplyMarkup = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ReplyInlineMarkup, pydantic.Tag('ReplyInlineMarkup')],
        typing.Annotated[types.ReplyKeyboardForceReply, pydantic.Tag('ReplyKeyboardForceReply')],
        typing.Annotated[types.ReplyKeyboardHide, pydantic.Tag('ReplyKeyboardHide')],
        typing.Annotated[types.ReplyKeyboardMarkup, pydantic.Tag('ReplyKeyboardMarkup')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
