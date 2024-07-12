from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# updates.ChannelDifference - Layer 181
ChannelDifference = typing.Annotated[
    typing.Union[
        typing.Annotated[types.updates.ChannelDifference, pydantic.Tag('updates.ChannelDifference')],
        typing.Annotated[types.updates.ChannelDifferenceEmpty, pydantic.Tag('updates.ChannelDifferenceEmpty')],
        typing.Annotated[types.updates.ChannelDifferenceTooLong, pydantic.Tag('updates.ChannelDifferenceTooLong')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
