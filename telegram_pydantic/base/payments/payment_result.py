from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# payments.PaymentResult - Layer 181
PaymentResult = typing.Annotated[
    typing.Union[
        typing.Annotated[types.payments.PaymentResult, pydantic.Tag('payments.PaymentResult')],
        typing.Annotated[types.payments.PaymentVerificationNeeded, pydantic.Tag('payments.PaymentVerificationNeeded')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
