from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFile(BaseModel):
    """
    functions.upload.GetFile
    ID: 0xbe5335be
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetFile', 'GetFile'] = pydantic.Field(
        'functions.upload.GetFile',
        alias='_'
    )

    location: "base.InputFileLocation"
    offset: int
    limit: int
    precise: typing.Optional[bool] = None
    cdn_supported: typing.Optional[bool] = None
