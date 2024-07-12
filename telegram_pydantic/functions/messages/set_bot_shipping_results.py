from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotShippingResults(BaseModel):
    """
    functions.messages.SetBotShippingResults
    ID: 0xe5f672fa
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetBotShippingResults', 'SetBotShippingResults'] = pydantic.Field(
        'functions.messages.SetBotShippingResults',
        alias='_'
    )

    query_id: int
    error: typing.Optional[str] = None
    shipping_options: typing.Optional[list["base.ShippingOption"]] = None
