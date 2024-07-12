from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PageListOrderedItem - Layer 181
PageListOrderedItem = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PageListOrderedItemBlocks, pydantic.Tag('PageListOrderedItemBlocks')],
        typing.Annotated[types.PageListOrderedItemText, pydantic.Tag('PageListOrderedItemText')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
