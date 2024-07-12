from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# AttachMenuBots - Layer 181
AttachMenuBots = typing.Annotated[
    typing.Union[
        typing.Annotated[types.AttachMenuBots, pydantic.Tag('AttachMenuBots')],
        typing.Annotated[types.AttachMenuBotsNotModified, pydantic.Tag('AttachMenuBotsNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
