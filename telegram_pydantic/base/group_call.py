from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# GroupCall - Layer 181
GroupCall = typing.Annotated[
    typing.Union[
        typing.Annotated[types.GroupCall, pydantic.Tag('GroupCall')],
        typing.Annotated[types.GroupCallDiscarded, pydantic.Tag('GroupCallDiscarded')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
