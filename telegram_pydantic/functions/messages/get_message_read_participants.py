from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessageReadParticipants(BaseModel):
    """
    functions.messages.GetMessageReadParticipants
    ID: 0x31c1c44f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessageReadParticipants', 'GetMessageReadParticipants'] = pydantic.Field(
        'functions.messages.GetMessageReadParticipants',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
