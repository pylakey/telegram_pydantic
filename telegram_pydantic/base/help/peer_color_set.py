from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.PeerColorSet - Layer 181
PeerColorSet = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.PeerColorProfileSet, pydantic.Tag('help.PeerColorProfileSet')],
        typing.Annotated[types.help.PeerColorSet, pydantic.Tag('help.PeerColorSet')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
