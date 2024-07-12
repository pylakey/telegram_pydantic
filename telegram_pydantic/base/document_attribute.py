from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# DocumentAttribute - Layer 181
DocumentAttribute = typing.Annotated[
    typing.Union[
        typing.Annotated[types.DocumentAttributeAnimated, pydantic.Tag('DocumentAttributeAnimated')],
        typing.Annotated[types.DocumentAttributeAudio, pydantic.Tag('DocumentAttributeAudio')],
        typing.Annotated[types.DocumentAttributeCustomEmoji, pydantic.Tag('DocumentAttributeCustomEmoji')],
        typing.Annotated[types.DocumentAttributeFilename, pydantic.Tag('DocumentAttributeFilename')],
        typing.Annotated[types.DocumentAttributeHasStickers, pydantic.Tag('DocumentAttributeHasStickers')],
        typing.Annotated[types.DocumentAttributeImageSize, pydantic.Tag('DocumentAttributeImageSize')],
        typing.Annotated[types.DocumentAttributeSticker, pydantic.Tag('DocumentAttributeSticker')],
        typing.Annotated[types.DocumentAttributeVideo, pydantic.Tag('DocumentAttributeVideo')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
