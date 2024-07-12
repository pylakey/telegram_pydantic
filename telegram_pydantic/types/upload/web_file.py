from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebFile(BaseModel):
    """
    types.upload.WebFile
    ID: 0x21e753bc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.WebFile', 'WebFile'] = pydantic.Field(
        'types.upload.WebFile',
        alias='_'
    )

    size: int
    mime_type: str
    file_type: "base.storage.FileType"
    mtime: int
    bytes: Bytes
