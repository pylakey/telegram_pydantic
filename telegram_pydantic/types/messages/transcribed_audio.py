from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TranscribedAudio(BaseModel):
    """
    types.messages.TranscribedAudio
    ID: 0xcfb9d957
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.TranscribedAudio', 'TranscribedAudio'] = pydantic.Field(
        'types.messages.TranscribedAudio',
        alias='_'
    )

    transcription_id: int
    text: str
    pending: typing.Optional[bool] = None
    trial_remains_num: typing.Optional[int] = None
    trial_remains_until_date: typing.Optional[Datetime] = None
