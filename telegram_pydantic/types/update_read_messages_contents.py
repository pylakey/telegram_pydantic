from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadMessagesContents(BaseModel):
    """
    types.UpdateReadMessagesContents
    ID: 0xf8227181
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadMessagesContents', 'UpdateReadMessagesContents'] = pydantic.Field(
        'types.UpdateReadMessagesContents',
        alias='_'
    )

    messages: list[int]
    pts: int
    pts_count: int
    date: typing.Optional[Datetime] = None
