from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveAppLog(BaseModel):
    """
    functions.help.SaveAppLog
    ID: 0x6f02f748
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.SaveAppLog', 'SaveAppLog'] = pydantic.Field(
        'functions.help.SaveAppLog',
        alias='_'
    )

    events: list["base.InputAppEvent"]
