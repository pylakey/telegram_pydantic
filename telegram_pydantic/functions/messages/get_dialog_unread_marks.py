from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDialogUnreadMarks(BaseModel):
    """
    functions.messages.GetDialogUnreadMarks
    ID: 0x22e24e22
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDialogUnreadMarks', 'GetDialogUnreadMarks'] = pydantic.Field(
        'functions.messages.GetDialogUnreadMarks',
        alias='_'
    )

