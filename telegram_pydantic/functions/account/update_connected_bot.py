from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateConnectedBot(BaseModel):
    """
    functions.account.UpdateConnectedBot
    ID: 0x43d8521d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateConnectedBot', 'UpdateConnectedBot'] = pydantic.Field(
        'functions.account.UpdateConnectedBot',
        alias='_'
    )

    bot: "base.InputUser"
    recipients: "base.InputBusinessBotRecipients"
    can_reply: typing.Optional[bool] = None
    deleted: typing.Optional[bool] = None
