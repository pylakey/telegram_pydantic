from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPremiumGiftCodeOptions(BaseModel):
    """
    functions.payments.GetPremiumGiftCodeOptions
    ID: 0x2757ba54
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetPremiumGiftCodeOptions', 'GetPremiumGiftCodeOptions'] = pydantic.Field(
        'functions.payments.GetPremiumGiftCodeOptions',
        alias='_'
    )

    boost_peer: typing.Optional["base.InputPeer"] = None
