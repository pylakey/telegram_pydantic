from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteHistory(BaseModel):
    """
    functions.channels.DeleteHistory
    ID: 0x9baa9647
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteHistory', 'DeleteHistory'] = pydantic.Field(
        'functions.channels.DeleteHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    max_id: int
    for_everyone: typing.Optional[bool] = None
