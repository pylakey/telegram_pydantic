from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputPaymentCredentials - Layer 181
InputPaymentCredentials = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputPaymentCredentials, pydantic.Tag('InputPaymentCredentials')],
        typing.Annotated[types.InputPaymentCredentialsApplePay, pydantic.Tag('InputPaymentCredentialsApplePay')],
        typing.Annotated[types.InputPaymentCredentialsGooglePay, pydantic.Tag('InputPaymentCredentialsGooglePay')],
        typing.Annotated[types.InputPaymentCredentialsSaved, pydantic.Tag('InputPaymentCredentialsSaved')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
