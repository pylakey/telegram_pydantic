from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonChildAbuse(BaseModel):
    """
    types.InputReportReasonChildAbuse
    ID: 0xadf44ee3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonChildAbuse', 'InputReportReasonChildAbuse'] = pydantic.Field(
        'types.InputReportReasonChildAbuse',
        alias='_'
    )

