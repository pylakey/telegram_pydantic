from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendReaction(BaseModel):
    """
    functions.messages.SendReaction
    ID: 0xd30d78d4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendReaction', 'SendReaction'] = pydantic.Field(
        'functions.messages.SendReaction',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    big: typing.Optional[bool] = None
    add_to_recent: typing.Optional[bool] = None
    reaction: typing.Optional[list["base.Reaction"]] = None
