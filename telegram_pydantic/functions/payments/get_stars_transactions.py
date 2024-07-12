from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStarsTransactions(BaseModel):
    """
    functions.payments.GetStarsTransactions
    ID: 0x673ac2f9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetStarsTransactions', 'GetStarsTransactions'] = pydantic.Field(
        'functions.payments.GetStarsTransactions',
        alias='_'
    )

    peer: "base.InputPeer"
    offset: str
    inbound: typing.Optional[bool] = None
    outbound: typing.Optional[bool] = None
