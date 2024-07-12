from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotUpdatesStatus(BaseModel):
    """
    functions.help.SetBotUpdatesStatus
    ID: 0xec22cfcd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.SetBotUpdatesStatus', 'SetBotUpdatesStatus'] = pydantic.Field(
        'functions.help.SetBotUpdatesStatus',
        alias='_'
    )

    pending_updates_count: int
    message: str
