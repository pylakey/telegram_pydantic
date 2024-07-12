from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveBigFilePart(BaseModel):
    """
    functions.upload.SaveBigFilePart
    ID: 0xde7b673d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.SaveBigFilePart', 'SaveBigFilePart'] = pydantic.Field(
        'functions.upload.SaveBigFilePart',
        alias='_'
    )

    file_id: int
    file_part: int
    file_total_parts: int
    bytes: Bytes
