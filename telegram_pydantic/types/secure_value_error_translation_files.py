from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueErrorTranslationFiles(BaseModel):
    """
    types.SecureValueErrorTranslationFiles
    ID: 0x34636dd8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueErrorTranslationFiles', 'SecureValueErrorTranslationFiles'] = pydantic.Field(
        'types.SecureValueErrorTranslationFiles',
        alias='_'
    )

    type: "base.SecureValueType"
    file_hash: list[Bytes]
    text: str
