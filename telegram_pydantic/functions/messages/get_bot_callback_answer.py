from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotCallbackAnswer(BaseModel):
    """
    functions.messages.GetBotCallbackAnswer
    ID: 0x9342ca07
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetBotCallbackAnswer', 'GetBotCallbackAnswer'] = pydantic.Field(
        'functions.messages.GetBotCallbackAnswer',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    game: typing.Optional[bool] = None
    data: typing.Optional[Bytes] = None
    password: typing.Optional["base.InputCheckPasswordSRP"] = None
