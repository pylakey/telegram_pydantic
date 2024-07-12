from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RateTranscribedAudio(BaseModel):
    """
    functions.messages.RateTranscribedAudio
    ID: 0x7f1d072f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RateTranscribedAudio', 'RateTranscribedAudio'] = pydantic.Field(
        'functions.messages.RateTranscribedAudio',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    transcription_id: int
    good: bool
