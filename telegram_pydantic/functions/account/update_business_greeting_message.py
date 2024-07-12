from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessGreetingMessage(BaseModel):
    """
    functions.account.UpdateBusinessGreetingMessage
    ID: 0x66cdafc4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessGreetingMessage', 'UpdateBusinessGreetingMessage'] = pydantic.Field(
        'functions.account.UpdateBusinessGreetingMessage',
        alias='_'
    )

    message: typing.Optional["base.InputBusinessGreetingMessage"] = None
