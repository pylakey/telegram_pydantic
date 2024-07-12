from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputBotInlineMessage - Layer 181
InputBotInlineMessage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputBotInlineMessageGame, pydantic.Tag('InputBotInlineMessageGame')],
        typing.Annotated[types.InputBotInlineMessageMediaAuto, pydantic.Tag('InputBotInlineMessageMediaAuto')],
        typing.Annotated[types.InputBotInlineMessageMediaContact, pydantic.Tag('InputBotInlineMessageMediaContact')],
        typing.Annotated[types.InputBotInlineMessageMediaGeo, pydantic.Tag('InputBotInlineMessageMediaGeo')],
        typing.Annotated[types.InputBotInlineMessageMediaInvoice, pydantic.Tag('InputBotInlineMessageMediaInvoice')],
        typing.Annotated[types.InputBotInlineMessageMediaVenue, pydantic.Tag('InputBotInlineMessageMediaVenue')],
        typing.Annotated[types.InputBotInlineMessageMediaWebPage, pydantic.Tag('InputBotInlineMessageMediaWebPage')],
        typing.Annotated[types.InputBotInlineMessageText, pydantic.Tag('InputBotInlineMessageText')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
