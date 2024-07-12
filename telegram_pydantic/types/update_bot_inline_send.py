from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotInlineSend(BaseModel):
    """
    types.UpdateBotInlineSend
    ID: 0x12f12a07
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotInlineSend', 'UpdateBotInlineSend'] = pydantic.Field(
        'types.UpdateBotInlineSend',
        alias='_'
    )

    user_id: int
    query: str
    id: str
    geo: typing.Optional["base.GeoPoint"] = None
    msg_id: typing.Optional["base.InputBotInlineMessageID"] = None
