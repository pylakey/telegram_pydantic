from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputChannel - Layer 181
InputChannel = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputChannel, pydantic.Tag('InputChannel')],
        typing.Annotated[types.InputChannelEmpty, pydantic.Tag('InputChannelEmpty')],
        typing.Annotated[types.InputChannelFromMessage, pydantic.Tag('InputChannelFromMessage')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
