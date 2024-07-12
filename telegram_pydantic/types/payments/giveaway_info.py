from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GiveawayInfo(BaseModel):
    """
    types.payments.GiveawayInfo
    ID: 0x4367daa0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.GiveawayInfo', 'GiveawayInfo'] = pydantic.Field(
        'types.payments.GiveawayInfo',
        alias='_'
    )

    start_date: Datetime
    participating: typing.Optional[bool] = None
    preparing_results: typing.Optional[bool] = None
    joined_too_early_date: Datetime
    admin_disallowed_chat_id: typing.Optional[int] = None
    disallowed_country: typing.Optional[str] = None
