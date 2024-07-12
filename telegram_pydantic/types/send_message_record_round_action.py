from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageRecordRoundAction(BaseModel):
    """
    types.SendMessageRecordRoundAction
    ID: 0x88f27fbc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageRecordRoundAction', 'SendMessageRecordRoundAction'] = pydantic.Field(
        'types.SendMessageRecordRoundAction',
        alias='_'
    )

