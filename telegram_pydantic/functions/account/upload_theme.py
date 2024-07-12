from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadTheme(BaseModel):
    """
    functions.account.UploadTheme
    ID: 0x1c3db333
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UploadTheme', 'UploadTheme'] = pydantic.Field(
        'functions.account.UploadTheme',
        alias='_'
    )

    file: "base.InputFile"
    file_name: str
    mime_type: str
    thumb: typing.Optional["base.InputFile"] = None
