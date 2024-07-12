from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateShortSentMessage(BaseModel):
    """
    types.UpdateShortSentMessage
    ID: 0x9015e101
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateShortSentMessage', 'UpdateShortSentMessage'] = pydantic.Field(
        'types.UpdateShortSentMessage',
        alias='_'
    )

    id: int
    pts: int
    pts_count: int
    date: Datetime
    out: typing.Optional[bool] = None
    media: typing.Optional["base.MessageMedia"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    ttl_period: typing.Optional[int] = None
