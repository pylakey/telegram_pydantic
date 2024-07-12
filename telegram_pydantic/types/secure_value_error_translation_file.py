from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorTranslationFile(BaseModel):
    """
    types.SecureValueErrorTranslationFile
    ID: 0xa1144770
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorTranslationFile', 'SecureValueErrorTranslationFile'] = pydantic.Field(
        'types.SecureValueErrorTranslationFile',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: Bytes
    text: str
