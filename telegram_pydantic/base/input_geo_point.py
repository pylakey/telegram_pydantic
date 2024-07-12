from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputGeoPoint - Layer 181
InputGeoPoint = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputGeoPoint, pydantic.Tag('InputGeoPoint')],
        typing.Annotated[types.InputGeoPointEmpty, pydantic.Tag('InputGeoPointEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
