from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReceivedNotifyMessage(BaseModel):
    """
    types.ReceivedNotifyMessage
    ID: 0xa384b779
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReceivedNotifyMessage', 'ReceivedNotifyMessage'] = pydantic.Field(
        'types.ReceivedNotifyMessage',
        alias='_'
    )

    id: int
    flags: int
