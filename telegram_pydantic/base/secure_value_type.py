from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SecureValueType - Layer 181
SecureValueType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SecureValueTypeAddress, pydantic.Tag('SecureValueTypeAddress')],
        typing.Annotated[types.SecureValueTypeBankStatement, pydantic.Tag('SecureValueTypeBankStatement')],
        typing.Annotated[types.SecureValueTypeDriverLicense, pydantic.Tag('SecureValueTypeDriverLicense')],
        typing.Annotated[types.SecureValueTypeEmail, pydantic.Tag('SecureValueTypeEmail')],
        typing.Annotated[types.SecureValueTypeIdentityCard, pydantic.Tag('SecureValueTypeIdentityCard')],
        typing.Annotated[types.SecureValueTypeInternalPassport, pydantic.Tag('SecureValueTypeInternalPassport')],
        typing.Annotated[types.SecureValueTypePassport, pydantic.Tag('SecureValueTypePassport')],
        typing.Annotated[types.SecureValueTypePassportRegistration, pydantic.Tag('SecureValueTypePassportRegistration')],
        typing.Annotated[types.SecureValueTypePersonalDetails, pydantic.Tag('SecureValueTypePersonalDetails')],
        typing.Annotated[types.SecureValueTypePhone, pydantic.Tag('SecureValueTypePhone')],
        typing.Annotated[types.SecureValueTypeRentalAgreement, pydantic.Tag('SecureValueTypeRentalAgreement')],
        typing.Annotated[types.SecureValueTypeTemporaryRegistration, pydantic.Tag('SecureValueTypeTemporaryRegistration')],
        typing.Annotated[types.SecureValueTypeUtilityBill, pydantic.Tag('SecureValueTypeUtilityBill')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
