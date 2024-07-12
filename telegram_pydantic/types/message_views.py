from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageViews(BaseModel):
    """
    types.MessageViews
    ID: 0x455b853d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageViews', 'MessageViews'] = pydantic.Field(
        'types.MessageViews',
        alias='_'
    )

    views: typing.Optional[int] = None
    forwards: typing.Optional[int] = None
    replies: typing.Optional["base.MessageReplies"] = None
