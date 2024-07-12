from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# WebPageAttribute - Layer 181
WebPageAttribute = typing.Annotated[
    typing.Union[
        typing.Annotated[types.WebPageAttributeStickerSet, pydantic.Tag('WebPageAttributeStickerSet')],
        typing.Annotated[types.WebPageAttributeStory, pydantic.Tag('WebPageAttributeStory')],
        typing.Annotated[types.WebPageAttributeTheme, pydantic.Tag('WebPageAttributeTheme')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
