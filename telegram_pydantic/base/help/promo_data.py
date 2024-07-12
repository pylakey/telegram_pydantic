from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.PromoData - Layer 181
PromoData = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.PromoData, pydantic.Tag('help.PromoData')],
        typing.Annotated[types.help.PromoDataEmpty, pydantic.Tag('help.PromoDataEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
