from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotWebhookJSON(BaseModel):
    """
    types.UpdateBotWebhookJSON
    ID: 0x8317c0c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotWebhookJSON', 'UpdateBotWebhookJSON'] = pydantic.Field(
        'types.UpdateBotWebhookJSON',
        alias='_'
    )

    data: "base.DataJSON"
