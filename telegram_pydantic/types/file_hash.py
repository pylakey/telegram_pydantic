from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileHash(BaseModel):
    """
    types.FileHash
    ID: 0xf39b035c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.FileHash', 'FileHash'] = pydantic.Field(
        'types.FileHash',
        alias='_'
    )

    offset: int
    limit: int
    hash: Bytes
