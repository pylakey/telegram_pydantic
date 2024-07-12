from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StartBot(BaseModel):
    """
    functions.messages.StartBot
    ID: 0xe6df7378
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.StartBot', 'StartBot'] = pydantic.Field(
        'functions.messages.StartBot',
        alias='_'
    )

    bot: "base.InputUser"
    peer: "base.InputPeer"
    random_id: int
    start_param: str
