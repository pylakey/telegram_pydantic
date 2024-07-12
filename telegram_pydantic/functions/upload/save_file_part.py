from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveFilePart(BaseModel):
    """
    functions.upload.SaveFilePart
    ID: 0xb304a621
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.SaveFilePart', 'SaveFilePart'] = pydantic.Field(
        'functions.upload.SaveFilePart',
        alias='_'
    )

    file_id: int
    file_part: int
    bytes: Bytes
