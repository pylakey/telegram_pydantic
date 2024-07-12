from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePlainPhone(BaseModel):
    """
    types.SecurePlainPhone
    ID: 0x7d6099dd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePlainPhone', 'SecurePlainPhone'] = pydantic.Field(
        'types.SecurePlainPhone',
        alias='_'
    )

    phone: str
