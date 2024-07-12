from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGiveawayInfo(BaseModel):
    """
    functions.payments.GetGiveawayInfo
    ID: 0xf4239425
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetGiveawayInfo', 'GetGiveawayInfo'] = pydantic.Field(
        'functions.payments.GetGiveawayInfo',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
