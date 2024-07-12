from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedDialogs(BaseModel):
    """
    functions.messages.GetSavedDialogs
    ID: 0x5381d21a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSavedDialogs', 'GetSavedDialogs'] = pydantic.Field(
        'functions.messages.GetSavedDialogs',
        alias='_'
    )

    offset_date: Datetime
    offset_id: int
    offset_peer: "base.InputPeer"
    limit: int
    hash: int
    exclude_pinned: typing.Optional[bool] = None
