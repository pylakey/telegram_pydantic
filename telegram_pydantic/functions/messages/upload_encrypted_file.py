from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadEncryptedFile(BaseModel):
    """
    functions.messages.UploadEncryptedFile
    ID: 0x5057c497
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UploadEncryptedFile', 'UploadEncryptedFile'] = pydantic.Field(
        'functions.messages.UploadEncryptedFile',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    file: "base.InputEncryptedFile"
