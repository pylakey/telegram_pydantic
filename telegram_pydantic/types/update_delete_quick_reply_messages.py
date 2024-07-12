from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteQuickReplyMessages(BaseModel):
    """
    types.UpdateDeleteQuickReplyMessages
    ID: 0x566fe7cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteQuickReplyMessages', 'UpdateDeleteQuickReplyMessages'] = pydantic.Field(
        'types.UpdateDeleteQuickReplyMessages',
        alias='_'
    )

    shortcut_id: int
    messages: list[int]
