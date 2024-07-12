from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.AppConfig - Layer 181
AppConfig = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.AppConfig, pydantic.Tag('help.AppConfig')],
        typing.Annotated[types.help.AppConfigNotModified, pydantic.Tag('help.AppConfigNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
