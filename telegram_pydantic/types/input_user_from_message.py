from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputUserFromMessage(BaseModel):
    """
    types.InputUserFromMessage
    ID: 0x1da448e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputUserFromMessage', 'InputUserFromMessage'] = pydantic.Field(
        'types.InputUserFromMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    user_id: int
