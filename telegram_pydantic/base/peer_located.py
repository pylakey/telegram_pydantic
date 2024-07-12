from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PeerLocated - Layer 181
PeerLocated = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PeerLocated, pydantic.Tag('PeerLocated')],
        typing.Annotated[types.PeerSelfLocated, pydantic.Tag('PeerSelfLocated')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
