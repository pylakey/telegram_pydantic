from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteParticipantHistory(BaseModel):
    """
    functions.channels.DeleteParticipantHistory
    ID: 0x367544db
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteParticipantHistory', 'DeleteParticipantHistory'] = pydantic.Field(
        'functions.channels.DeleteParticipantHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
