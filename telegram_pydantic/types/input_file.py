from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputFile(BaseModel):
    """
    types.InputFile
    ID: 0xf52ff27f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputFile', 'InputFile'] = pydantic.Field(
        'types.InputFile',
        alias='_'
    )

    id: int
    parts: int
    name: str
    md5_checksum: str
