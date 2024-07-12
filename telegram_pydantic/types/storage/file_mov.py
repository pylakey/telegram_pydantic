from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileMov(BaseModel):
    """
    types.storage.FileMov
    ID: 0x4b09ebbc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileMov', 'FileMov'] = pydantic.Field(
        'types.storage.FileMov',
        alias='_'
    )

