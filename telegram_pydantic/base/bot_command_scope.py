from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BotCommandScope - Layer 181
BotCommandScope = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BotCommandScopeChatAdmins, pydantic.Tag('BotCommandScopeChatAdmins')],
        typing.Annotated[types.BotCommandScopeChats, pydantic.Tag('BotCommandScopeChats')],
        typing.Annotated[types.BotCommandScopeDefault, pydantic.Tag('BotCommandScopeDefault')],
        typing.Annotated[types.BotCommandScopePeer, pydantic.Tag('BotCommandScopePeer')],
        typing.Annotated[types.BotCommandScopePeerAdmins, pydantic.Tag('BotCommandScopePeerAdmins')],
        typing.Annotated[types.BotCommandScopePeerUser, pydantic.Tag('BotCommandScopePeerUser')],
        typing.Annotated[types.BotCommandScopeUsers, pydantic.Tag('BotCommandScopeUsers')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
