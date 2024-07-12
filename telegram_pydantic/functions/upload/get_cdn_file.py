from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCdnFile(BaseModel):
    """
    functions.upload.GetCdnFile
    ID: 0x395f69da
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetCdnFile', 'GetCdnFile'] = pydantic.Field(
        'functions.upload.GetCdnFile',
        alias='_'
    )

    file_token: Bytes
    offset: int
    limit: int
