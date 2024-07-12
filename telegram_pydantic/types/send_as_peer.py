from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendAsPeer(BaseModel):
    """
    types.SendAsPeer
    ID: 0xb81c7034
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendAsPeer', 'SendAsPeer'] = pydantic.Field(
        'types.SendAsPeer',
        alias='_'
    )

    peer: "base.Peer"
    premium_required: typing.Optional[bool] = None
