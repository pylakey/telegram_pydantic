from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BlockFromReplies(BaseModel):
    """
    functions.contacts.BlockFromReplies
    ID: 0x29a8962c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.BlockFromReplies', 'BlockFromReplies'] = pydantic.Field(
        'functions.contacts.BlockFromReplies',
        alias='_'
    )

    msg_id: int
    delete_message: typing.Optional[bool] = None
    delete_history: typing.Optional[bool] = None
    report_spam: typing.Optional[bool] = None
