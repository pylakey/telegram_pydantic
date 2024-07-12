from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# UserProfilePhoto - Layer 181
UserProfilePhoto = typing.Annotated[
    typing.Union[
        typing.Annotated[types.UserProfilePhoto, pydantic.Tag('UserProfilePhoto')],
        typing.Annotated[types.UserProfilePhotoEmpty, pydantic.Tag('UserProfilePhotoEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
