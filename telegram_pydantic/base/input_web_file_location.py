from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputWebFileLocation - Layer 181
InputWebFileLocation = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputWebFileAudioAlbumThumbLocation, pydantic.Tag('InputWebFileAudioAlbumThumbLocation')],
        typing.Annotated[types.InputWebFileGeoPointLocation, pydantic.Tag('InputWebFileGeoPointLocation')],
        typing.Annotated[types.InputWebFileLocation, pydantic.Tag('InputWebFileLocation')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
