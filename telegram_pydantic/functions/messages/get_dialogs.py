from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDialogs(BaseModel):
    """
    functions.messages.GetDialogs
    ID: 0xa0f4cb4f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDialogs', 'GetDialogs'] = pydantic.Field(
        'functions.messages.GetDialogs',
        alias='_'
    )

    offset_date: Datetime
    offset_id: int
    offset_peer: "base.InputPeer"
    limit: int
    hash: int
    exclude_pinned: typing.Optional[bool] = None
    folder_id: typing.Optional[int] = None
