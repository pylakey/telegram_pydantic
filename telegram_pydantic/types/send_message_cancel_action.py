from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageCancelAction(BaseModel):
    """
    types.SendMessageCancelAction
    ID: 0xfd5ec8f5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageCancelAction', 'SendMessageCancelAction'] = pydantic.Field(
        'types.SendMessageCancelAction',
        alias='_'
    )

