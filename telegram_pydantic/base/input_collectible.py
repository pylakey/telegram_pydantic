from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputCollectible - Layer 181
InputCollectible = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputCollectiblePhone, pydantic.Tag('InputCollectiblePhone')],
        typing.Annotated[types.InputCollectibleUsername, pydantic.Tag('InputCollectibleUsername')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
