from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InitTakeoutSession(BaseModel):
    """
    functions.account.InitTakeoutSession
    ID: 0x8ef3eab0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.InitTakeoutSession', 'InitTakeoutSession'] = pydantic.Field(
        'functions.account.InitTakeoutSession',
        alias='_'
    )

    contacts: typing.Optional[bool] = None
    message_users: typing.Optional[bool] = None
    message_chats: typing.Optional[bool] = None
    message_megagroups: typing.Optional[bool] = None
    message_channels: typing.Optional[bool] = None
    files: typing.Optional[bool] = None
    file_max_size: typing.Optional[int] = None
