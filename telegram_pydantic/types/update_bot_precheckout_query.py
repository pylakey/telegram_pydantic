from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotPrecheckoutQuery(BaseModel):
    """
    types.UpdateBotPrecheckoutQuery
    ID: 0x8caa9a96
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotPrecheckoutQuery', 'UpdateBotPrecheckoutQuery'] = pydantic.Field(
        'types.UpdateBotPrecheckoutQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    payload: Bytes
    currency: str
    total_amount: int
    info: typing.Optional["base.PaymentRequestedInfo"] = None
    shipping_option_id: typing.Optional[str] = None
