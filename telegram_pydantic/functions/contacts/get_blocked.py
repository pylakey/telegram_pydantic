from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBlocked(BaseModel):
    """
    functions.contacts.GetBlocked
    ID: 0x9a868f80
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetBlocked', 'GetBlocked'] = pydantic.Field(
        'functions.contacts.GetBlocked',
        alias='_'
    )

    offset: int
    limit: int
    my_stories_from: typing.Optional[bool] = None
