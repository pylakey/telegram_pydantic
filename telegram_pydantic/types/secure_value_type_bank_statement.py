from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypeBankStatement(BaseModel):
    """
    types.SecureValueTypeBankStatement
    ID: 0x89137c0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypeBankStatement', 'SecureValueTypeBankStatement'] = pydantic.Field(
        'types.SecureValueTypeBankStatement',
        alias='_'
    )

