from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChannelLocation - Layer 181
ChannelLocation = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChannelLocation, pydantic.Tag('ChannelLocation')],
        typing.Annotated[types.ChannelLocationEmpty, pydantic.Tag('ChannelLocationEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
