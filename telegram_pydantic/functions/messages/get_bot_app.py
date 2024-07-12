from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBotApp(BaseModel):
    """
    functions.messages.GetBotApp
    ID: 0x34fdc5c3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetBotApp', 'GetBotApp'] = pydantic.Field(
        'functions.messages.GetBotApp',
        alias='_'
    )

    app: "base.InputBotApp"
    hash: int
