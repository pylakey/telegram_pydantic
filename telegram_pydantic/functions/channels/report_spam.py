from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportSpam(BaseModel):
    """
    functions.channels.ReportSpam
    ID: 0xf44a8315
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReportSpam', 'ReportSpam'] = pydantic.Field(
        'functions.channels.ReportSpam',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
    id: list[int]
