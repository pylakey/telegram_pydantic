from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class File(BaseModel):
    """
    types.upload.File
    ID: 0x96a18d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.File', 'File'] = pydantic.Field(
        'types.upload.File',
        alias='_'
    )

    type: "base.storage.FileType"
    mtime: int
    bytes: Bytes
