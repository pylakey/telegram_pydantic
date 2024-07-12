from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputInvoice - Layer 181
InputInvoice = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputInvoiceMessage, pydantic.Tag('InputInvoiceMessage')],
        typing.Annotated[types.InputInvoicePremiumGiftCode, pydantic.Tag('InputInvoicePremiumGiftCode')],
        typing.Annotated[types.InputInvoiceSlug, pydantic.Tag('InputInvoiceSlug')],
        typing.Annotated[types.InputInvoiceStars, pydantic.Tag('InputInvoiceStars')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
