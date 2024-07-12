from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# updates.Difference - Layer 181
Difference = typing.Annotated[
    typing.Union[
        typing.Annotated[types.updates.Difference, pydantic.Tag('updates.Difference')],
        typing.Annotated[types.updates.DifferenceEmpty, pydantic.Tag('updates.DifferenceEmpty')],
        typing.Annotated[types.updates.DifferenceSlice, pydantic.Tag('updates.DifferenceSlice')],
        typing.Annotated[types.updates.DifferenceTooLong, pydantic.Tag('updates.DifferenceTooLong')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
