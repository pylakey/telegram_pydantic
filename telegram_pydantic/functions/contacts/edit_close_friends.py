from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditCloseFriends(BaseModel):
    """
    functions.contacts.EditCloseFriends
    ID: 0xba6705f0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.EditCloseFriends', 'EditCloseFriends'] = pydantic.Field(
        'functions.contacts.EditCloseFriends',
        alias='_'
    )

    id: list[int]
