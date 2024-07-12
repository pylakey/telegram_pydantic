from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotWebhookJSONQuery(BaseModel):
    """
    types.UpdateBotWebhookJSONQuery
    ID: 0x9b9240a6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotWebhookJSONQuery', 'UpdateBotWebhookJSONQuery'] = pydantic.Field(
        'types.UpdateBotWebhookJSONQuery',
        alias='_'
    )

    query_id: int
    data: "base.DataJSON"
    timeout: int
