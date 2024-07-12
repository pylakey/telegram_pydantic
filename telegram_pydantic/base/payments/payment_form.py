from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# payments.PaymentForm - Layer 181
PaymentForm = typing.Annotated[
    typing.Union[
        typing.Annotated[types.payments.PaymentForm, pydantic.Tag('payments.PaymentForm')],
        typing.Annotated[types.payments.PaymentFormStars, pydantic.Tag('payments.PaymentFormStars')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
