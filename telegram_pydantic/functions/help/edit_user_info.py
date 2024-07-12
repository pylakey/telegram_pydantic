from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditUserInfo(BaseModel):
    """
    functions.help.EditUserInfo
    ID: 0x66b91b70
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.EditUserInfo', 'EditUserInfo'] = pydantic.Field(
        'functions.help.EditUserInfo',
        alias='_'
    )

    user_id: "base.InputUser"
    message: str
    entities: list["base.MessageEntity"]
