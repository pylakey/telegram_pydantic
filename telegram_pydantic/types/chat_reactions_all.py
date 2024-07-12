from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatReactionsAll(BaseModel):
    """
    types.ChatReactionsAll
    ID: 0x52928bca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatReactionsAll', 'ChatReactionsAll'] = pydantic.Field(
        'types.ChatReactionsAll',
        alias='_'
    )

    allow_custom: typing.Optional[bool] = None
