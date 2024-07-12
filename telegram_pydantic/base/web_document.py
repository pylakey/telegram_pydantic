from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# WebDocument - Layer 181
WebDocument = typing.Annotated[
    typing.Union[
        typing.Annotated[types.WebDocument, pydantic.Tag('WebDocument')],
        typing.Annotated[types.WebDocumentNoProxy, pydantic.Tag('WebDocumentNoProxy')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
