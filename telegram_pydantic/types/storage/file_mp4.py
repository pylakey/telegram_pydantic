from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileMp4(BaseModel):
    """
    types.storage.FileMp4
    ID: 0xb3cea0e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileMp4', 'FileMp4'] = pydantic.Field(
        'types.storage.FileMp4',
        alias='_'
    )

