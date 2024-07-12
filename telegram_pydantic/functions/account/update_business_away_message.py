from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessAwayMessage(BaseModel):
    """
    functions.account.UpdateBusinessAwayMessage
    ID: 0xa26a7fa5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessAwayMessage', 'UpdateBusinessAwayMessage'] = pydantic.Field(
        'functions.account.UpdateBusinessAwayMessage',
        alias='_'
    )

    message: typing.Optional["base.InputBusinessAwayMessage"] = None
