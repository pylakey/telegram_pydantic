from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveCallLog(BaseModel):
    """
    functions.phone.SaveCallLog
    ID: 0x41248786
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SaveCallLog', 'SaveCallLog'] = pydantic.Field(
        'functions.phone.SaveCallLog',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    file: "base.InputFile"
