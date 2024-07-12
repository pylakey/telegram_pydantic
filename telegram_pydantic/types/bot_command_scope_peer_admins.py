from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopePeerAdmins(BaseModel):
    """
    types.BotCommandScopePeerAdmins
    ID: 0x3fd863d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopePeerAdmins', 'BotCommandScopePeerAdmins'] = pydantic.Field(
        'types.BotCommandScopePeerAdmins',
        alias='_'
    )

    peer: "base.InputPeer"
