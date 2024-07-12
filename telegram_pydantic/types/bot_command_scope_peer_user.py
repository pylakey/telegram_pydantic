from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopePeerUser(BaseModel):
    """
    types.BotCommandScopePeerUser
    ID: 0xa1321f3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopePeerUser', 'BotCommandScopePeerUser'] = pydantic.Field(
        'types.BotCommandScopePeerUser',
        alias='_'
    )

    peer: "base.InputPeer"
    user_id: "base.InputUser"
