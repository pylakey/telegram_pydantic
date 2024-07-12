from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBoostsStatus(BaseModel):
    """
    functions.premium.GetBoostsStatus
    ID: 0x42f1f61
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetBoostsStatus', 'GetBoostsStatus'] = pydantic.Field(
        'functions.premium.GetBoostsStatus',
        alias='_'
    )

    peer: "base.InputPeer"
