from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckHistoryImport(BaseModel):
    """
    functions.messages.CheckHistoryImport
    ID: 0x43fe19f3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckHistoryImport', 'CheckHistoryImport'] = pydantic.Field(
        'functions.messages.CheckHistoryImport',
        alias='_'
    )

    import_head: str
