from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeAudio(BaseModel):
    """
    types.DocumentAttributeAudio
    ID: 0x9852f9c6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeAudio', 'DocumentAttributeAudio'] = pydantic.Field(
        'types.DocumentAttributeAudio',
        alias='_'
    )

    duration: int
    voice: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    performer: typing.Optional[str] = None
    waveform: typing.Optional[Bytes] = None
