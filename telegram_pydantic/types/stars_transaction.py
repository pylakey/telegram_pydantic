from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransaction(BaseModel):
    """
    types.StarsTransaction
    ID: 0xcc7079b2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransaction', 'StarsTransaction'] = pydantic.Field(
        'types.StarsTransaction',
        alias='_'
    )

    id: str
    stars: int
    date: Datetime
    peer: "base.StarsTransactionPeer"
    refund: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    photo: typing.Optional["base.WebDocument"] = None
