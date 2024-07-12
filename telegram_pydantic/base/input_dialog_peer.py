from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputDialogPeer - Layer 181
InputDialogPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputDialogPeer, pydantic.Tag('InputDialogPeer')],
        typing.Annotated[types.InputDialogPeerFolder, pydantic.Tag('InputDialogPeerFolder')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
