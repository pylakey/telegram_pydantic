from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Document - Layer 181
Document = typing.Annotated[
    typing.Union[
        typing.Annotated[types.Document, pydantic.Tag('Document')],
        typing.Annotated[types.DocumentEmpty, pydantic.Tag('DocumentEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
