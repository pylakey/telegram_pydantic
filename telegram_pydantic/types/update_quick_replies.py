from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateQuickReplies(BaseModel):
    """
    types.UpdateQuickReplies
    ID: 0xf9470ab2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateQuickReplies', 'UpdateQuickReplies'] = pydantic.Field(
        'types.UpdateQuickReplies',
        alias='_'
    )

    quick_replies: list["base.QuickReply"]
