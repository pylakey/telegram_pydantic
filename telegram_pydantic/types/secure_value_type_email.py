from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeEmail(BaseModel):
    """
    types.SecureValueTypeEmail
    ID: 0x8e3ca7ee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeEmail', 'SecureValueTypeEmail'] = pydantic.Field(
        'types.SecureValueTypeEmail',
        alias='_'
    )

