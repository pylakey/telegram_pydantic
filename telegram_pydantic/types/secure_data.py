from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureData(BaseModel):
    """
    types.SecureData
    ID: 0x8aeabec3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureData', 'SecureData'] = pydantic.Field(
        'types.SecureData',
        alias='_'
    )

    data: Bytes
    data_hash: Bytes
    secret: Bytes
