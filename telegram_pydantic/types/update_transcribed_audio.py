from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateTranscribedAudio(BaseModel):
    """
    types.UpdateTranscribedAudio
    ID: 0x84cd5a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateTranscribedAudio', 'UpdateTranscribedAudio'] = pydantic.Field(
        'types.UpdateTranscribedAudio',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    transcription_id: int
    text: str
    pending: typing.Optional[bool] = None
