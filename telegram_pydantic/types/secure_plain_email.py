from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePlainEmail(BaseModel):
    """
    types.SecurePlainEmail
    ID: 0x21ec5a5f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePlainEmail', 'SecurePlainEmail'] = pydantic.Field(
        'types.SecurePlainEmail',
        alias='_'
    )

    email: str
