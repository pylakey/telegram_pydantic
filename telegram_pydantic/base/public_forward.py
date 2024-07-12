from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PublicForward - Layer 181
PublicForward = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PublicForwardMessage, pydantic.Tag('PublicForwardMessage')],
        typing.Annotated[types.PublicForwardStory, pydantic.Tag('PublicForwardStory')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
