from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotChatBoost(BaseModel):
    """
    types.UpdateBotChatBoost
    ID: 0x904dd49c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotChatBoost', 'UpdateBotChatBoost'] = pydantic.Field(
        'types.UpdateBotChatBoost',
        alias='_'
    )

    peer: "base.Peer"
    boost: "base.Boost"
    qts: int
