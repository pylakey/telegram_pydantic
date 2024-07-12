from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeTemporaryRegistration(BaseModel):
    """
    types.SecureValueTypeTemporaryRegistration
    ID: 0xea02ec33
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeTemporaryRegistration', 'SecureValueTypeTemporaryRegistration'] = pydantic.Field(
        'types.SecureValueTypeTemporaryRegistration',
        alias='_'
    )

