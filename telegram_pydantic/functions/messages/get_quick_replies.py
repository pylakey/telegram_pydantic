from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetQuickReplies(BaseModel):
    """
    functions.messages.GetQuickReplies
    ID: 0xd483f2a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetQuickReplies', 'GetQuickReplies'] = pydantic.Field(
        'functions.messages.GetQuickReplies',
        alias='_'
    )

    hash: int
