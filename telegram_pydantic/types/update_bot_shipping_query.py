from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotShippingQuery(BaseModel):
    """
    types.UpdateBotShippingQuery
    ID: 0xb5aefd7d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotShippingQuery', 'UpdateBotShippingQuery'] = pydantic.Field(
        'types.UpdateBotShippingQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    payload: Bytes
    shipping_address: "base.PostAddress"
