from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueHash(BaseModel):
    """
    types.SecureValueHash
    ID: 0xed1ecdb0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueHash', 'SecureValueHash'] = pydantic.Field(
        'types.SecureValueHash',
        alias='_'
    )

    type: "base.SecureValueType"
    hash: Bytes
