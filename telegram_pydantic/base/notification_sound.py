from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# NotificationSound - Layer 181
NotificationSound = typing.Annotated[
    typing.Union[
        typing.Annotated[types.NotificationSoundDefault, pydantic.Tag('NotificationSoundDefault')],
        typing.Annotated[types.NotificationSoundLocal, pydantic.Tag('NotificationSoundLocal')],
        typing.Annotated[types.NotificationSoundNone, pydantic.Tag('NotificationSoundNone')],
        typing.Annotated[types.NotificationSoundRingtone, pydantic.Tag('NotificationSoundRingtone')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
