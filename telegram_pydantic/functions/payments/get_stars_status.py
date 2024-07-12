from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStarsStatus(BaseModel):
    """
    functions.payments.GetStarsStatus
    ID: 0x104fcfa7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetStarsStatus', 'GetStarsStatus'] = pydantic.Field(
        'functions.payments.GetStarsStatus',
        alias='_'
    )

    peer: "base.InputPeer"
