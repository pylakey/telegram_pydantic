from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateQuickReplyMessage(BaseModel):
    """
    types.UpdateQuickReplyMessage
    ID: 0x3e050d0f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateQuickReplyMessage', 'UpdateQuickReplyMessage'] = pydantic.Field(
        'types.UpdateQuickReplyMessage',
        alias='_'
    )

    message: "base.Message"
