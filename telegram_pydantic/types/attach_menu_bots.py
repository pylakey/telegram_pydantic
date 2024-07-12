from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBots(BaseModel):
    """
    types.AttachMenuBots
    ID: 0x3c4301c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBots', 'AttachMenuBots'] = pydantic.Field(
        'types.AttachMenuBots',
        alias='_'
    )

    hash: int
    bots: list["base.AttachMenuBot"]
    users: list["base.User"]
