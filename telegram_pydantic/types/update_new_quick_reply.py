from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewQuickReply(BaseModel):
    """
    types.UpdateNewQuickReply
    ID: 0xf53da717
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewQuickReply', 'UpdateNewQuickReply'] = pydantic.Field(
        'types.UpdateNewQuickReply',
        alias='_'
    )

    quick_reply: "base.QuickReply"
