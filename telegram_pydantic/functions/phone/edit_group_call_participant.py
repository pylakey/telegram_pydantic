from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditGroupCallParticipant(BaseModel):
    """
    functions.phone.EditGroupCallParticipant
    ID: 0xa5273abf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.EditGroupCallParticipant', 'EditGroupCallParticipant'] = pydantic.Field(
        'functions.phone.EditGroupCallParticipant',
        alias='_'
    )

    call: "base.InputGroupCall"
    participant: "base.InputPeer"
    muted: typing.Optional[bool] = None
    volume: typing.Optional[int] = None
    raise_hand: typing.Optional[bool] = None
    video_stopped: typing.Optional[bool] = None
    video_paused: typing.Optional[bool] = None
    presentation_paused: typing.Optional[bool] = None
