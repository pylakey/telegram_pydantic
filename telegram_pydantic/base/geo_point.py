from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# GeoPoint - Layer 181
GeoPoint = typing.Annotated[
    typing.Union[
        typing.Annotated[types.GeoPoint, pydantic.Tag('GeoPoint')],
        typing.Annotated[types.GeoPointEmpty, pydantic.Tag('GeoPointEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
