from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckedGiftCode(BaseModel):
    """
    types.payments.CheckedGiftCode
    ID: 0x284a1096
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.CheckedGiftCode', 'CheckedGiftCode'] = pydantic.Field(
        'types.payments.CheckedGiftCode',
        alias='_'
    )

    date: Datetime
    months: int
    chats: list["base.Chat"]
    users: list["base.User"]
    via_giveaway: typing.Optional[bool] = None
    from_id: typing.Optional["base.Peer"] = None
    giveaway_msg_id: typing.Optional[int] = None
    to_id: typing.Optional[int] = None
    used_date: typing.Optional[Datetime] = None
