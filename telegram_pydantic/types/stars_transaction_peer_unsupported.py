from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeerUnsupported(BaseModel):
    """
    types.StarsTransactionPeerUnsupported
    ID: 0x95f2bfe4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeerUnsupported', 'StarsTransactionPeerUnsupported'] = pydantic.Field(
        'types.StarsTransactionPeerUnsupported',
        alias='_'
    )

