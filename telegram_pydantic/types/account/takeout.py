from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Takeout(BaseModel):
    """
    types.account.Takeout
    ID: 0x4dba4501
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.Takeout', 'Takeout'] = pydantic.Field(
        'types.account.Takeout',
        alias='_'
    )

    id: int
