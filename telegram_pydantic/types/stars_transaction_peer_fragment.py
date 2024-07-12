from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeerFragment(BaseModel):
    """
    types.StarsTransactionPeerFragment
    ID: 0xe92fd902
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeerFragment', 'StarsTransactionPeerFragment'] = pydantic.Field(
        'types.StarsTransactionPeerFragment',
        alias='_'
    )

