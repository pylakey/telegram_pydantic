from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureFile(BaseModel):
    """
    types.SecureFile
    ID: 0x7d09c27e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureFile', 'SecureFile'] = pydantic.Field(
        'types.SecureFile',
        alias='_'
    )

    id: int
    access_hash: int
    size: int
    dc_id: int
    date: Datetime
    file_hash: Bytes
    secret: Bytes
