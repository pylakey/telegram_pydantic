from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotMessageReaction(BaseModel):
    """
    types.UpdateBotMessageReaction
    ID: 0xac21d3ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotMessageReaction', 'UpdateBotMessageReaction'] = pydantic.Field(
        'types.UpdateBotMessageReaction',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    date: Datetime
    actor: "base.Peer"
    old_reactions: list["base.Reaction"]
    new_reactions: list["base.Reaction"]
    qts: int
