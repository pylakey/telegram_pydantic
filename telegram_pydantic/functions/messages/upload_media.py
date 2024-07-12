from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadMedia(BaseModel):
    """
    functions.messages.UploadMedia
    ID: 0x14967978
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UploadMedia', 'UploadMedia'] = pydantic.Field(
        'functions.messages.UploadMedia',
        alias='_'
    )

    peer: "base.InputPeer"
    media: "base.InputMedia"
    business_connection_id: typing.Optional[str] = None
