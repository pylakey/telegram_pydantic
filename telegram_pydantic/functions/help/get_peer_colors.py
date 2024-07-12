from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerColors(BaseModel):
    """
    functions.help.GetPeerColors
    ID: 0xda80f42f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPeerColors', 'GetPeerColors'] = pydantic.Field(
        'functions.help.GetPeerColors',
        alias='_'
    )

    hash: int
