from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BotInlineMessage - Layer 181
BotInlineMessage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BotInlineMessageMediaAuto, pydantic.Tag('BotInlineMessageMediaAuto')],
        typing.Annotated[types.BotInlineMessageMediaContact, pydantic.Tag('BotInlineMessageMediaContact')],
        typing.Annotated[types.BotInlineMessageMediaGeo, pydantic.Tag('BotInlineMessageMediaGeo')],
        typing.Annotated[types.BotInlineMessageMediaInvoice, pydantic.Tag('BotInlineMessageMediaInvoice')],
        typing.Annotated[types.BotInlineMessageMediaVenue, pydantic.Tag('BotInlineMessageMediaVenue')],
        typing.Annotated[types.BotInlineMessageMediaWebPage, pydantic.Tag('BotInlineMessageMediaWebPage')],
        typing.Annotated[types.BotInlineMessageText, pydantic.Tag('BotInlineMessageText')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
