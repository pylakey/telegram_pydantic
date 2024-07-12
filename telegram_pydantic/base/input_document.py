from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputDocument - Layer 181
InputDocument = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputDocument, pydantic.Tag('InputDocument')],
        typing.Annotated[types.InputDocumentEmpty, pydantic.Tag('InputDocumentEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
