from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageRecordAudioAction(BaseModel):
    """
    types.SendMessageRecordAudioAction
    ID: 0xd52f73f7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageRecordAudioAction', 'SendMessageRecordAudioAction'] = pydantic.Field(
        'types.SendMessageRecordAudioAction',
        alias='_'
    )

