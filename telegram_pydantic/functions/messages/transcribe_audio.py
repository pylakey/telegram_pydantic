from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TranscribeAudio(BaseModel):
    """
    functions.messages.TranscribeAudio
    ID: 0x269e9a49
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.TranscribeAudio', 'TranscribeAudio'] = pydantic.Field(
        'functions.messages.TranscribeAudio',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
