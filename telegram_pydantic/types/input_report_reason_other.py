from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonOther(BaseModel):
    """
    types.InputReportReasonOther
    ID: 0xc1e4a2b1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonOther', 'InputReportReasonOther'] = pydantic.Field(
        'types.InputReportReasonOther',
        alias='_'
    )

