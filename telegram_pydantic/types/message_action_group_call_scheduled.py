from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGroupCallScheduled(BaseModel):
    """
    types.MessageActionGroupCallScheduled
    ID: 0xb3a07661
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGroupCallScheduled', 'MessageActionGroupCallScheduled'] = pydantic.Field(
        'types.MessageActionGroupCallScheduled',
        alias='_'
    )

    call: "base.InputGroupCall"
    schedule_date: Datetime
