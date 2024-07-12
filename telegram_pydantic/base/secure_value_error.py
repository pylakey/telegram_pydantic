from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SecureValueError - Layer 181
SecureValueError = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SecureValueError, pydantic.Tag('SecureValueError')],
        typing.Annotated[types.SecureValueErrorData, pydantic.Tag('SecureValueErrorData')],
        typing.Annotated[types.SecureValueErrorFile, pydantic.Tag('SecureValueErrorFile')],
        typing.Annotated[types.SecureValueErrorFiles, pydantic.Tag('SecureValueErrorFiles')],
        typing.Annotated[types.SecureValueErrorFrontSide, pydantic.Tag('SecureValueErrorFrontSide')],
        typing.Annotated[types.SecureValueErrorReverseSide, pydantic.Tag('SecureValueErrorReverseSide')],
        typing.Annotated[types.SecureValueErrorSelfie, pydantic.Tag('SecureValueErrorSelfie')],
        typing.Annotated[types.SecureValueErrorTranslationFile, pydantic.Tag('SecureValueErrorTranslationFile')],
        typing.Annotated[types.SecureValueErrorTranslationFiles, pydantic.Tag('SecureValueErrorTranslationFiles')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
