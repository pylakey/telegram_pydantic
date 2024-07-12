from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BusinessAwayMessage(BaseModel):
    """
    types.BusinessAwayMessage
    ID: 0xef156a5c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BusinessAwayMessage', 'BusinessAwayMessage'] = pydantic.Field(
        'types.BusinessAwayMessage',
        alias='_'
    )

    shortcut_id: int
    schedule: "base.BusinessAwayMessageSchedule"
    recipients: "base.BusinessRecipients"
    offline_only: typing.Optional[bool] = None
