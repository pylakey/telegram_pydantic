from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotApp(BaseModel):
    """
    types.messages.BotApp
    ID: 0xeb50adf5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.BotApp', 'BotApp'] = pydantic.Field(
        'types.messages.BotApp',
        alias='_'
    )

    app: "base.BotApp"
    inactive: typing.Optional[bool] = None
    request_write_access: typing.Optional[bool] = None
    has_settings: typing.Optional[bool] = None
