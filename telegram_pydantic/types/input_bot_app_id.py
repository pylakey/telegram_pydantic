from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotAppID(BaseModel):
    """
    types.InputBotAppID
    ID: 0xa920bd7a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotAppID', 'InputBotAppID'] = pydantic.Field(
        'types.InputBotAppID',
        alias='_'
    )

    id: int
    access_hash: int
