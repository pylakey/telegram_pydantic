from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteMessages(BaseModel):
    """
    types.UpdateDeleteMessages
    ID: 0xa20db0e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteMessages', 'UpdateDeleteMessages'] = pydantic.Field(
        'types.UpdateDeleteMessages',
        alias='_'
    )

    messages: list[int]
    pts: int
    pts_count: int
