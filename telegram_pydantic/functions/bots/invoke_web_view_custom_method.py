from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWebViewCustomMethod(BaseModel):
    """
    functions.bots.InvokeWebViewCustomMethod
    ID: 0x87fc5e7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.InvokeWebViewCustomMethod', 'InvokeWebViewCustomMethod'] = pydantic.Field(
        'functions.bots.InvokeWebViewCustomMethod',
        alias='_'
    )

    bot: "base.InputUser"
    custom_method: str
    params: "base.DataJSON"
