from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetRecentLocations(BaseModel):
    """
    functions.messages.GetRecentLocations
    ID: 0x702a40e0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetRecentLocations', 'GetRecentLocations'] = pydantic.Field(
        'functions.messages.GetRecentLocations',
        alias='_'
    )

    peer: "base.InputPeer"
    limit: int
    hash: int
