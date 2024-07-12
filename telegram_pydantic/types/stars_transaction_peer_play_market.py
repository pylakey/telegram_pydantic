from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeerPlayMarket(BaseModel):
    """
    types.StarsTransactionPeerPlayMarket
    ID: 0x7b560a0b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeerPlayMarket', 'StarsTransactionPeerPlayMarket'] = pydantic.Field(
        'types.StarsTransactionPeerPlayMarket',
        alias='_'
    )

