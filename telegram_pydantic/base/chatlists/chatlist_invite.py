from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# chatlists.ChatlistInvite - Layer 181
ChatlistInvite = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.chatlists.ChatlistInvite,
            pydantic.Tag('chatlists.ChatlistInvite'),
            pydantic.Tag('ChatlistInvite')
        ],
        typing.Annotated[
            types.chatlists.ChatlistInviteAlready,
            pydantic.Tag('chatlists.ChatlistInviteAlready'),
            pydantic.Tag('ChatlistInviteAlready')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
