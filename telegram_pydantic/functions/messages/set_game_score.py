from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetGameScore(BaseModel):
    """
    functions.messages.SetGameScore
    ID: 0x8ef8ecc0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetGameScore', 'SetGameScore'] = pydantic.Field(
        'functions.messages.SetGameScore',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    user_id: "base.InputUser"
    score: int
    edit_message: typing.Optional[bool] = None
    force: typing.Optional[bool] = None
