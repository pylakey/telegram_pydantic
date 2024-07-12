from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeIdentityCard(BaseModel):
    """
    types.SecureValueTypeIdentityCard
    ID: 0xa0d0744b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeIdentityCard', 'SecureValueTypeIdentityCard'] = pydantic.Field(
        'types.SecureValueTypeIdentityCard',
        alias='_'
    )

