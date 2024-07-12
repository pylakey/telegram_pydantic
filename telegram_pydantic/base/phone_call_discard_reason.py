from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PhoneCallDiscardReason - Layer 181
PhoneCallDiscardReason = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PhoneCallDiscardReasonBusy, pydantic.Tag('PhoneCallDiscardReasonBusy')],
        typing.Annotated[types.PhoneCallDiscardReasonDisconnect, pydantic.Tag('PhoneCallDiscardReasonDisconnect')],
        typing.Annotated[types.PhoneCallDiscardReasonHangup, pydantic.Tag('PhoneCallDiscardReasonHangup')],
        typing.Annotated[types.PhoneCallDiscardReasonMissed, pydantic.Tag('PhoneCallDiscardReasonMissed')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
