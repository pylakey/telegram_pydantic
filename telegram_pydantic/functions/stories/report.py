from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Report(BaseModel):
    """
    functions.stories.Report
    ID: 0x1923fa8c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.Report', 'Report'] = pydantic.Field(
        'functions.stories.Report',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
    reason: "base.ReportReason"
    message: str
