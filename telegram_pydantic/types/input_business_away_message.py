from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessAwayMessage(BaseModel):
    """
    types.InputBusinessAwayMessage
    ID: 0x832175e0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessAwayMessage', 'InputBusinessAwayMessage'] = pydantic.Field(
        'types.InputBusinessAwayMessage',
        alias='_'
    )

    shortcut_id: int
    schedule: "base.BusinessAwayMessageSchedule"
    recipients: "base.InputBusinessRecipients"
    offline_only: typing.Optional[bool] = None
