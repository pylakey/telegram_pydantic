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
    functions.messages.ReportSpam
    ID: 0xcf1592db
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReportSpam', 'ReportSpam'] = pydantic.Field(
        'functions.messages.ReportSpam',
        alias='_'
    )

    peer: "base.InputPeer"
