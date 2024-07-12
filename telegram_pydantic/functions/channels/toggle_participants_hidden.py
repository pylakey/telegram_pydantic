from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleParticipantsHidden(BaseModel):
    """
    functions.channels.ToggleParticipantsHidden
    ID: 0x6a6e7854
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleParticipantsHidden', 'ToggleParticipantsHidden'] = pydantic.Field(
        'functions.channels.ToggleParticipantsHidden',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
