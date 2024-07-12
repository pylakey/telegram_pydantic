from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserTyping(BaseModel):
    """
    types.UpdateUserTyping
    ID: 0xc01e857f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserTyping', 'UpdateUserTyping'] = pydantic.Field(
        'types.UpdateUserTyping',
        alias='_'
    )

    user_id: int
    action: "base.SendMessageAction"
