from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckHistoryImportPeer(BaseModel):
    """
    functions.messages.CheckHistoryImportPeer
    ID: 0x5dc60f03
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckHistoryImportPeer', 'CheckHistoryImportPeer'] = pydantic.Field(
        'functions.messages.CheckHistoryImportPeer',
        alias='_'
    )

    peer: "base.InputPeer"
