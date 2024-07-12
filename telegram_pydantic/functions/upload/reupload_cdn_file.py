from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReuploadCdnFile(BaseModel):
    """
    functions.upload.ReuploadCdnFile
    ID: 0x9b2754a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.ReuploadCdnFile', 'ReuploadCdnFile'] = pydantic.Field(
        'functions.upload.ReuploadCdnFile',
        alias='_'
    )

    file_token: Bytes
    request_token: Bytes
