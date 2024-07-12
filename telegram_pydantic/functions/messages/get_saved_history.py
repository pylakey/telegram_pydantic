from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedHistory(BaseModel):
    """
    functions.messages.GetSavedHistory
    ID: 0x3d9a414d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSavedHistory', 'GetSavedHistory'] = pydantic.Field(
        'functions.messages.GetSavedHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    offset_date: Datetime
    add_offset: int
    limit: int
    max_id: int
    min_id: int
    hash: int
