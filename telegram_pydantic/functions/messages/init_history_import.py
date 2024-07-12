from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InitHistoryImport(BaseModel):
    """
    functions.messages.InitHistoryImport
    ID: 0x34090c3b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.InitHistoryImport', 'InitHistoryImport'] = pydantic.Field(
        'functions.messages.InitHistoryImport',
        alias='_'
    )

    peer: "base.InputPeer"
    file: "base.InputFile"
    media_count: int
