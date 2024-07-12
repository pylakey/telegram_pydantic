from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetParticipant(BaseModel):
    """
    functions.channels.GetParticipant
    ID: 0xa0ab6cc6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetParticipant', 'GetParticipant'] = pydantic.Field(
        'functions.channels.GetParticipant',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
