from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputPhoto - Layer 181
InputPhoto = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputPhoto, pydantic.Tag('InputPhoto')],
        typing.Annotated[types.InputPhotoEmpty, pydantic.Tag('InputPhotoEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
