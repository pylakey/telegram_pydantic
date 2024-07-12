from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.SavedRingtone - Layer 181
SavedRingtone = typing.Annotated[
    typing.Union[
        typing.Annotated[types.account.SavedRingtone, pydantic.Tag('account.SavedRingtone')],
        typing.Annotated[types.account.SavedRingtoneConverted, pydantic.Tag('account.SavedRingtoneConverted')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
