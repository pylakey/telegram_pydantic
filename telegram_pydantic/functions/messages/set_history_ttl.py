from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetHistoryTTL(BaseModel):
    """
    functions.messages.SetHistoryTTL
    ID: 0xb80e5fe4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetHistoryTTL', 'SetHistoryTTL'] = pydantic.Field(
        'functions.messages.SetHistoryTTL',
        alias='_'
    )

    peer: "base.InputPeer"
    period: int
