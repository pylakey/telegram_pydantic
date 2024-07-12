from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewScheduledMessage(BaseModel):
    """
    types.UpdateNewScheduledMessage
    ID: 0x39a51dfb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewScheduledMessage', 'UpdateNewScheduledMessage'] = pydantic.Field(
        'types.UpdateNewScheduledMessage',
        alias='_'
    )

    message: "base.Message"
