from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AnswerWebhookJSONQuery(BaseModel):
    """
    functions.bots.AnswerWebhookJSONQuery
    ID: 0xe6213f4d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.AnswerWebhookJSONQuery', 'AnswerWebhookJSONQuery'] = pydantic.Field(
        'functions.bots.AnswerWebhookJSONQuery',
        alias='_'
    )

    query_id: int
    data: "base.DataJSON"
