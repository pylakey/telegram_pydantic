from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HistoryImport(BaseModel):
    """
    types.messages.HistoryImport
    ID: 0x1662af0b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.HistoryImport', 'HistoryImport'] = pydantic.Field(
        'types.messages.HistoryImport',
        alias='_'
    )

    id: int
