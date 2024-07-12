from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonViolence(BaseModel):
    """
    types.InputReportReasonViolence
    ID: 0x1e22c78d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonViolence', 'InputReportReasonViolence'] = pydantic.Field(
        'types.InputReportReasonViolence',
        alias='_'
    )

