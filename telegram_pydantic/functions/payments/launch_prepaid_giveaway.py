from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LaunchPrepaidGiveaway(BaseModel):
    """
    functions.payments.LaunchPrepaidGiveaway
    ID: 0x5ff58f20
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.LaunchPrepaidGiveaway', 'LaunchPrepaidGiveaway'] = pydantic.Field(
        'functions.payments.LaunchPrepaidGiveaway',
        alias='_'
    )

    peer: "base.InputPeer"
    giveaway_id: int
    purpose: "base.InputStorePaymentPurpose"
