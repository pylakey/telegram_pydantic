from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputBotApp - Layer 181
InputBotApp = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputBotAppID, pydantic.Tag('InputBotAppID')],
        typing.Annotated[types.InputBotAppShortName, pydantic.Tag('InputBotAppShortName')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
