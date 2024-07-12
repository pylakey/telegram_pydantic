from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.SavedRingtones - Layer 181
SavedRingtones = typing.Annotated[
    typing.Union[
        typing.Annotated[types.account.SavedRingtones, pydantic.Tag('account.SavedRingtones')],
        typing.Annotated[types.account.SavedRingtonesNotModified, pydantic.Tag('account.SavedRingtonesNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
