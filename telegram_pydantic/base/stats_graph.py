from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# StatsGraph - Layer 181
StatsGraph = typing.Annotated[
    typing.Union[
        typing.Annotated[types.StatsGraph, pydantic.Tag('StatsGraph')],
        typing.Annotated[types.StatsGraphAsync, pydantic.Tag('StatsGraphAsync')],
        typing.Annotated[types.StatsGraphError, pydantic.Tag('StatsGraphError')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
