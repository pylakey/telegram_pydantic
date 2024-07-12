from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadImportedMedia(BaseModel):
    """
    functions.messages.UploadImportedMedia
    ID: 0x2a862092
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UploadImportedMedia', 'UploadImportedMedia'] = pydantic.Field(
        'functions.messages.UploadImportedMedia',
        alias='_'
    )

    peer: "base.InputPeer"
    import_id: int
    file_name: str
    media: "base.InputMedia"
