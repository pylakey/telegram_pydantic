from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# DialogPeer - Layer 181
DialogPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.DialogPeer, pydantic.Tag('DialogPeer')],
        typing.Annotated[types.DialogPeerFolder, pydantic.Tag('DialogPeerFolder')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
