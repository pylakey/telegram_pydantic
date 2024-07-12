from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotDeleteBusinessMessage(BaseModel):
    """
    types.UpdateBotDeleteBusinessMessage
    ID: 0xa02a982e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotDeleteBusinessMessage', 'UpdateBotDeleteBusinessMessage'] = pydantic.Field(
        'types.UpdateBotDeleteBusinessMessage',
        alias='_'
    )

    connection_id: str
    peer: "base.Peer"
    messages: list[int]
    qts: int
