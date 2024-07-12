from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBoostsList(BaseModel):
    """
    functions.premium.GetBoostsList
    ID: 0x60f67660
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetBoostsList', 'GetBoostsList'] = pydantic.Field(
        'functions.premium.GetBoostsList',
        alias='_'
    )

    peer: "base.InputPeer"
    offset: str
    limit: int
    gifts: typing.Optional[bool] = None
