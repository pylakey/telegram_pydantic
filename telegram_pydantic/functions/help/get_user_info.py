from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUserInfo(BaseModel):
    """
    functions.help.GetUserInfo
    ID: 0x38a08d3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetUserInfo', 'GetUserInfo'] = pydantic.Field(
        'functions.help.GetUserInfo',
        alias='_'
    )

    user_id: "base.InputUser"
