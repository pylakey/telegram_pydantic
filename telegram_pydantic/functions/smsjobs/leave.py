from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Leave(BaseModel):
    """
    functions.smsjobs.Leave
    ID: 0x9898ad73
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.Leave', 'Leave'] = pydantic.Field(
        'functions.smsjobs.Leave',
        alias='_'
    )

