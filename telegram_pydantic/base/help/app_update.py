from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.AppUpdate - Layer 181
AppUpdate = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.AppUpdate, pydantic.Tag('help.AppUpdate')],
        typing.Annotated[types.help.NoAppUpdate, pydantic.Tag('help.NoAppUpdate')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
