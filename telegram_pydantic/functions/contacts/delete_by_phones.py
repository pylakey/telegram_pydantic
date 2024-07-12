from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteByPhones(BaseModel):
    """
    functions.contacts.DeleteByPhones
    ID: 0x1013fd9e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.DeleteByPhones', 'DeleteByPhones'] = pydantic.Field(
        'functions.contacts.DeleteByPhones',
        alias='_'
    )

    phones: list[str]
