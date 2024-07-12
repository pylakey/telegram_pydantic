from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypePassportRegistration(BaseModel):
    """
    types.SecureValueTypePassportRegistration
    ID: 0x99e3806a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypePassportRegistration', 'SecureValueTypePassportRegistration'] = pydantic.Field(
        'types.SecureValueTypePassportRegistration',
        alias='_'
    )

