from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatReactionsNone(BaseModel):
    """
    types.ChatReactionsNone
    ID: 0xeafc32bc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatReactionsNone', 'ChatReactionsNone'] = pydantic.Field(
        'types.ChatReactionsNone',
        alias='_'
    )

