from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendWebViewData(BaseModel):
    """
    functions.messages.SendWebViewData
    ID: 0xdc0242c8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendWebViewData', 'SendWebViewData'] = pydantic.Field(
        'functions.messages.SendWebViewData',
        alias='_'
    )

    bot: "base.InputUser"
    random_id: int
    button_text: str
    data: str
