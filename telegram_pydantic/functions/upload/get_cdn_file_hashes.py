from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCdnFileHashes(BaseModel):
    """
    functions.upload.GetCdnFileHashes
    ID: 0x91dc3f31
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetCdnFileHashes', 'GetCdnFileHashes'] = pydantic.Field(
        'functions.upload.GetCdnFileHashes',
        alias='_'
    )

    file_token: Bytes
    offset: int
