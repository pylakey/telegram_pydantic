from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# StickerSetCovered - Layer 181
StickerSetCovered = typing.Annotated[
    typing.Union[
        typing.Annotated[types.StickerSetCovered, pydantic.Tag('StickerSetCovered')],
        typing.Annotated[types.StickerSetFullCovered, pydantic.Tag('StickerSetFullCovered')],
        typing.Annotated[types.StickerSetMultiCovered, pydantic.Tag('StickerSetMultiCovered')],
        typing.Annotated[types.StickerSetNoCovered, pydantic.Tag('StickerSetNoCovered')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
