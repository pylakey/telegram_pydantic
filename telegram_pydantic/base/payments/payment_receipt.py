from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# payments.PaymentReceipt - Layer 181
PaymentReceipt = typing.Annotated[
    typing.Union[
        typing.Annotated[types.payments.PaymentReceipt, pydantic.Tag('payments.PaymentReceipt')],
        typing.Annotated[types.payments.PaymentReceiptStars, pydantic.Tag('payments.PaymentReceiptStars')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
