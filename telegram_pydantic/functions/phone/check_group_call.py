from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckGroupCall(BaseModel):
    """
    functions.phone.CheckGroupCall
    ID: 0xb59cf977
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.CheckGroupCall', 'CheckGroupCall'] = pydantic.Field(
        'functions.phone.CheckGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    sources: list[int]
