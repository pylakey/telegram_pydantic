from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# payments.GiveawayInfo - Layer 181
GiveawayInfo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.payments.GiveawayInfo, pydantic.Tag('payments.GiveawayInfo')],
        typing.Annotated[types.payments.GiveawayInfoResults, pydantic.Tag('payments.GiveawayInfoResults')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
