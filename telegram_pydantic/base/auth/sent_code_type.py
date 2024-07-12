from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# auth.SentCodeType - Layer 181
SentCodeType = typing.Annotated[
    typing.Union[
        typing.Annotated[types.auth.SentCodeTypeApp, pydantic.Tag('auth.SentCodeTypeApp')],
        typing.Annotated[types.auth.SentCodeTypeCall, pydantic.Tag('auth.SentCodeTypeCall')],
        typing.Annotated[types.auth.SentCodeTypeEmailCode, pydantic.Tag('auth.SentCodeTypeEmailCode')],
        typing.Annotated[types.auth.SentCodeTypeFirebaseSms, pydantic.Tag('auth.SentCodeTypeFirebaseSms')],
        typing.Annotated[types.auth.SentCodeTypeFlashCall, pydantic.Tag('auth.SentCodeTypeFlashCall')],
        typing.Annotated[types.auth.SentCodeTypeFragmentSms, pydantic.Tag('auth.SentCodeTypeFragmentSms')],
        typing.Annotated[types.auth.SentCodeTypeMissedCall, pydantic.Tag('auth.SentCodeTypeMissedCall')],
        typing.Annotated[types.auth.SentCodeTypeSetUpEmailRequired, pydantic.Tag('auth.SentCodeTypeSetUpEmailRequired')],
        typing.Annotated[types.auth.SentCodeTypeSms, pydantic.Tag('auth.SentCodeTypeSms')],
        typing.Annotated[types.auth.SentCodeTypeSmsPhrase, pydantic.Tag('auth.SentCodeTypeSmsPhrase')],
        typing.Annotated[types.auth.SentCodeTypeSmsWord, pydantic.Tag('auth.SentCodeTypeSmsWord')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
