from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateServiceNotification(BaseModel):
    """
    types.UpdateServiceNotification
    ID: 0xebe46819
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateServiceNotification', 'UpdateServiceNotification'] = pydantic.Field(
        'types.UpdateServiceNotification',
        alias='_'
    )

    type: str
    message: str
    media: "base.MessageMedia"
    entities: list["base.MessageEntity"]
    popup: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    inbox_date: Datetime
