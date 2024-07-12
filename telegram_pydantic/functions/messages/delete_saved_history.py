from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteSavedHistory(BaseModel):
    """
    functions.messages.DeleteSavedHistory
    ID: 0x6e98102b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteSavedHistory', 'DeleteSavedHistory'] = pydantic.Field(
        'functions.messages.DeleteSavedHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    max_id: int
    min_date: typing.Optional[Datetime] = None
    max_date: typing.Optional[Datetime] = None
