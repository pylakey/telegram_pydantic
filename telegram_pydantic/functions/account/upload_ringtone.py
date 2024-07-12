from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadRingtone(BaseModel):
    """
    functions.account.UploadRingtone
    ID: 0x831a83a2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UploadRingtone', 'UploadRingtone'] = pydantic.Field(
        'functions.account.UploadRingtone',
        alias='_'
    )

    file: "base.InputFile"
    file_name: str
    mime_type: str
