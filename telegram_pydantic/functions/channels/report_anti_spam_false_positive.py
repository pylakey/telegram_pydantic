from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportAntiSpamFalsePositive(BaseModel):
    """
    functions.channels.ReportAntiSpamFalsePositive
    ID: 0xa850a693
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReportAntiSpamFalsePositive', 'ReportAntiSpamFalsePositive'] = pydantic.Field(
        'functions.channels.ReportAntiSpamFalsePositive',
        alias='_'
    )

    channel: "base.InputChannel"
    msg_id: int
