from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStorePaymentPremiumGiveaway(BaseModel):
    """
    types.InputStorePaymentPremiumGiveaway
    ID: 0x160544ca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStorePaymentPremiumGiveaway', 'InputStorePaymentPremiumGiveaway'] = pydantic.Field(
        'types.InputStorePaymentPremiumGiveaway',
        alias='_'
    )

    boost_peer: "base.InputPeer"
    random_id: int
    until_date: Datetime
    currency: str
    amount: int
    only_new_subscribers: typing.Optional[bool] = None
    winners_are_visible: typing.Optional[bool] = None
    additional_peers: typing.Optional[list["base.InputPeer"]] = None
    countries_iso2: typing.Optional[list[str]] = None
    prize_description: typing.Optional[str] = None
