from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvokeWithoutUpdates(BaseModel):
    """
    functions.InvokeWithoutUpdates
    ID: 0xbf9459b7
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InvokeWithoutUpdates', 'InvokeWithoutUpdates'] = pydantic.Field(
        'functions.InvokeWithoutUpdates',
        alias='_'
    )

    query: BaseModel
