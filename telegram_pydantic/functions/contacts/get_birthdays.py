from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBirthdays(BaseModel):
    """
    functions.contacts.GetBirthdays
    ID: 0xdaeda864
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetBirthdays', 'GetBirthdays'] = pydantic.Field(
        'functions.contacts.GetBirthdays',
        alias='_'
    )

