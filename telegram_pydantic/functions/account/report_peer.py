from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportPeer(BaseModel):
    """
    functions.account.ReportPeer
    ID: 0xc5ba3d86
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ReportPeer', 'ReportPeer'] = pydantic.Field(
        'functions.account.ReportPeer',
        alias='_'
    )

    peer: "base.InputPeer"
    reason: "base.ReportReason"
    message: str
