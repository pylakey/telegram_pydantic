from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputStorePaymentPurpose - Layer 181
InputStorePaymentPurpose = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputStorePaymentGiftPremium, pydantic.Tag('InputStorePaymentGiftPremium')],
        typing.Annotated[types.InputStorePaymentPremiumGiftCode, pydantic.Tag('InputStorePaymentPremiumGiftCode')],
        typing.Annotated[types.InputStorePaymentPremiumGiveaway, pydantic.Tag('InputStorePaymentPremiumGiveaway')],
        typing.Annotated[types.InputStorePaymentPremiumSubscription, pydantic.Tag('InputStorePaymentPremiumSubscription')],
        typing.Annotated[types.InputStorePaymentStars, pydantic.Tag('InputStorePaymentStars')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
