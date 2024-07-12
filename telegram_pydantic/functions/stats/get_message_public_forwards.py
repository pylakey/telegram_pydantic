from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessagePublicForwards(BaseModel):
    """
    functions.stats.GetMessagePublicForwards
    ID: 0x5f150144
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stats.GetMessagePublicForwards', 'GetMessagePublicForwards'] = pydantic.Field(
        'functions.stats.GetMessagePublicForwards',
        alias='_'
    )

    channel: "base.InputChannel"
    msg_id: int
    offset: str
    limit: int
