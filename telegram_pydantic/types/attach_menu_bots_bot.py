from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBotsBot(BaseModel):
    """
    types.AttachMenuBotsBot
    ID: 0x93bf667f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBotsBot', 'AttachMenuBotsBot'] = pydantic.Field(
        'types.AttachMenuBotsBot',
        alias='_'
    )

    bot: "base.AttachMenuBot"
    users: list["base.User"]
