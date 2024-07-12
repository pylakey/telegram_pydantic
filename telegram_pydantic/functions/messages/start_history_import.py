from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StartHistoryImport(BaseModel):
    """
    functions.messages.StartHistoryImport
    ID: 0xb43df344
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.StartHistoryImport', 'StartHistoryImport'] = pydantic.Field(
        'functions.messages.StartHistoryImport',
        alias='_'
    )

    peer: "base.InputPeer"
    import_id: int
