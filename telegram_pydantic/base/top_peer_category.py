from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# TopPeerCategory - Layer 181
TopPeerCategory = typing.Annotated[
    typing.Union[
        typing.Annotated[types.TopPeerCategoryBotsInline, pydantic.Tag('TopPeerCategoryBotsInline')],
        typing.Annotated[types.TopPeerCategoryBotsPM, pydantic.Tag('TopPeerCategoryBotsPM')],
        typing.Annotated[types.TopPeerCategoryChannels, pydantic.Tag('TopPeerCategoryChannels')],
        typing.Annotated[types.TopPeerCategoryCorrespondents, pydantic.Tag('TopPeerCategoryCorrespondents')],
        typing.Annotated[types.TopPeerCategoryForwardChats, pydantic.Tag('TopPeerCategoryForwardChats')],
        typing.Annotated[types.TopPeerCategoryForwardUsers, pydantic.Tag('TopPeerCategoryForwardUsers')],
        typing.Annotated[types.TopPeerCategoryGroups, pydantic.Tag('TopPeerCategoryGroups')],
        typing.Annotated[types.TopPeerCategoryPhoneCalls, pydantic.Tag('TopPeerCategoryPhoneCalls')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
