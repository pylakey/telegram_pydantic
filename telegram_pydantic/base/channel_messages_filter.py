from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChannelMessagesFilter - Layer 181
ChannelMessagesFilter = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChannelMessagesFilter, pydantic.Tag('ChannelMessagesFilter')],
        typing.Annotated[types.ChannelMessagesFilterEmpty, pydantic.Tag('ChannelMessagesFilterEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
