from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadAudioAction(BaseModel):
    """
    types.SendMessageUploadAudioAction
    ID: 0xf351d7ab
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadAudioAction', 'SendMessageUploadAudioAction'] = pydantic.Field(
        'types.SendMessageUploadAudioAction',
        alias='_'
    )

    progress: int
