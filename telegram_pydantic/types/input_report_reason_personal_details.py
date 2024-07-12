from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonPersonalDetails(BaseModel):
    """
    types.InputReportReasonPersonalDetails
    ID: 0x9ec7863d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonPersonalDetails', 'InputReportReasonPersonalDetails'] = pydantic.Field(
        'types.InputReportReasonPersonalDetails',
        alias='_'
    )

