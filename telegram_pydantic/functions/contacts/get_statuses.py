from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStatuses(BaseModel):
    """
    functions.contacts.GetStatuses
    ID: 0xc4a353ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetStatuses', 'GetStatuses'] = pydantic.Field(
        'functions.contacts.GetStatuses',
        alias='_'
    )

